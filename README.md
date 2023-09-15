# ClassifiedsApp
WIP Idea from Yuki and Ramon

## Run:
* Any system w/ `python3` and `pip` or `pip3`:
    * `make python`
    * `make run`
* Debian (full deploy)
    * `make services python`
    * Edit `/etc/nginx/sites-enabled/classified.site` if needed, and `sudo systemctl restart nginx`
    * If edits are made to Python source, then `sudo systemctl restart classified`

# This project has moved:
[GitLab Repository](https://gitlab.mattcompton.dev/matt/ClassifiedsApp)