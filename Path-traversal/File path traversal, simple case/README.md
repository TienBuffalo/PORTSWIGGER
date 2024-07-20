## File path traversal, simple case
***
![](../images/1-1.png)

Ứng dụng web load ảnh của các post thông qua tham số filename.

![](../images/1-2.png)

Truy cập đường dẫn load ảnh của post bất kì. Ảnh này có vẻ nằm ở đường dẫn /var/www/html (web root directory của Linux).

Thay đổi tham số filename thành ../../../etc/passwd để traverse về thư mục root và truy cập file /etc/passwd.

![](../images/1-3.png)