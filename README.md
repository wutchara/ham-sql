Microsoft SQL
```
docker run --name ham-ms-sql -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=P@ssWord!" -p 1433:1433 -d mcr.microsoft.com/mssql/server
```

MYSQL
```
docker run --name ham-mysql -e MYSQL_ROOT_PASSWORD=P@ssWord! -d mysql
```

https://medium.com/@chrischuck35/how-to-create-a-mysql-instance-with-docker-compose-1598f3cc1bee

