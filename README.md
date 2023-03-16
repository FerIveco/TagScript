# TagScript
Scripts to automate resource tagging in Databricks

# Requirements
- Databricks-cli installed in environment
- Databricks must be configured to access 
 
# Databricks-cli installation
 
 Run pip install databricks-cli using the appropriate version of pip for your Python installation:
 
 ```
 pip install databricks-cli
 ```
 
 Upgrade databricks-cli
```
pip install databricks-cli --upgrade
```

# Set up authentication

```
databricks configure --token
```

- Enter your workspace URL, with the format **https://<instance-name>.cloud.databricks.com**. To get your workspace URL, see Workspace instance names, URLs, and IDs.<br>
**N.B.** when prompting the access token, characters will not appear, be sure to paste the token only one time

- After you complete the prompts, your access credentials are stored in the file **~/.databrickscfg** on Unix, Linux, or macOS, or **%USERPROFILE%\.databrickscfg** on Windows. The file contains a default profile entry:

```
[DEFAULT]
host = <workspace-URL>
token = <personal-access-token>
```

- If you prompted the wrong token in the configuration setup, you can change it directly from the .config file