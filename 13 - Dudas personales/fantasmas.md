```dataview
LIST WITHOUT ID link(meta(out).path) FLATTEN file.outlinks as out WHERE!(out.file) AND!contains(meta(out).path, "/") GROUP BY out SORT meta(out).path ASC
```