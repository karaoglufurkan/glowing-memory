# Simple File Organizer

- This python project categorizes all files in the specified directory(and in all child directories) by creating folders with extension names like jpeg, pdf, etc...

- Folder names and extensions are specified in **config.json** file.

- Keys represents categorization folder names and values are specified for identifying extensions

- For example, when you put the following object in the config.json file, the application creates a folder named **"python"** to the specified destination and copies all files ending with **"py"**, **"python"** or **"pyt"** to the created folder.

  
```json
{
	"python" : ["py", "python", "pyt"]
}
```

* All you need to do is to change config file as you wish and specify your source and target folder paths in main.py file. Then, all of a sudden, your all files in that source path are categorized in target folder by file type.


* In order to run the app, on terminal;

```console
{
    $ python main.py
}
```

## Dependencies

* python2 or python3