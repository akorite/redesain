// ch14_links.c -- names vs inodes: hard link, symlink, and unlink of an open file.
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
static void show(const char *label, const char *path) {
    struct stat st;
    if (stat(path, &st) < 0) { printf("%-9s %-8s  (no such name)\n", label, path); return; }
    printf("%-9s %-8s  ino=%-8lu nlink=%lu size=%ld\n", label, path,
           (unsigned long)st.st_ino, (unsigned long)st.st_nlink, (long)st.st_size);
}
int main(void) {
    char dir[] = "/tmp/ch14_links_XXXXXX";
    if (!mkdtemp(dir)) { perror("mkdtemp"); return 1; }
    if (chdir(dir) < 0) { perror("chdir"); return 1; }
    int fd = open("a", O_RDWR | O_CREAT, 0644);
    if (write(fd, "hello inode\n", 12) != 12) return 1;
    show("created",  "a");
    link("a", "b");                       // hard link: second NAME for the same inode
    show("link a->b", "a"); show("", "b");
    symlink("a", "s");                    // symlink: a new inode whose content is the text "a"
    struct stat ls; lstat("s", &ls);
    printf("symlink   s         ino=%-8lu is-symlink=%d size=%ld (length of the text \"a\")\n",
           (unsigned long)ls.st_ino, S_ISLNK(ls.st_mode) != 0, (long)ls.st_size);
    unlink("a"); unlink("b");             // remove both names; fd is still open
    show("unlinked", "a");
    char buf[32] = {0};
    ssize_t n = pread(fd, buf, sizeof buf - 1, 0);
    printf("read via still-open fd: %zd bytes: %s", n, buf);
    struct stat fs; fstat(fd, &fs);
    printf("fstat(fd): nlink=%lu (data lives until close)\n", (unsigned long)fs.st_nlink);
    close(fd);                            // last reference gone -> kernel frees the inode
    unlink("s"); rmdir(dir);
    return 0;
}
