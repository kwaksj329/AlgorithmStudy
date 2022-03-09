# PostgreSQL  

## 2022. 03. 03 version

### Creating  relations  (tables)  in  SQL

```sql
Create Table  Student(ID,  name,  GPA, photo)

Create Table  College (name string,  state char(2), enrollment integer)
```

### Query Languages

```sql
Select  Student.ID From Student, Apply Where Student.ID=Apply.ID And GPA>3.7 and college=‘Stanford’
```

