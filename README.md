# sample jupyterbook

Sample template for a Jupyter Book

## Usage

If you'd like to use this template for your own book:

### Create a repo copy of the template

1. Create your own repository on GitHub. Go here https://github.com/PACEHackWeek/sample-jupyterbook-repository and click on the green "Template" button in the top right. This will create a copy of the template with all the files in your GitHub account (or org).
2. In your repo, go to Settings (cog in the top nav) and click on Actions > General in the sidebar. Make sure "Allow all actions and reusable workflows" is checked.
3. Go to Settings and click on Pages. Under Build and deployment > Source, select "GitHub Actions". You don't need to change any other settings.
4. Go to the "About" section on your repo in the right bar and click the 'cog'. You will see "Use your GitHub Pages website" and a checkbox. Check that box. If it is checked already, then uncheck and re-check it. This will add the url to your book.

### Clone your copy of the template

1. Clone your repository. `git clone https://github.com/<your account>/<your reponame>`
2. If you are not on the CryoCloud hub run: `pip install -r requirements.txt`
3. Edit the books source files located in the `book/` directory
4. Push the changes up to GitHub.
5. On GitHub, click the Actions tab to watch the book build. When the workflow is done, you can click the url to see your book.

If the Action does not run, then you will need to debug. Click on the Action that did not build and click on the part that had a problem.


### Building your book locally

1. Open a terminal.
2. Run `jupyter-book clean book/` to remove any existing builds
3. Run `jupyter-book build book/`

A fully-rendered HTML version of the book will be built in `book/_build/html/`.

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).
