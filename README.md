# My-Spotify-Wrapped
The project aimed to create a personalized version of Spotify Wrapped, which summarizes a user's listening history for the year. The project used airflow for orchestration, Docker for containerization, dbt for modeling and transforming data, and GitHub Actions for continuous integration and delivery. The goal was to extract the user's listening history data from Spotify's API, transform it, and load it into a database. The transformed data would then be used to generate personalized insights and visualizations summarizing the user's listening history. The project aimed to provide a fun and engaging way for users to reflect on their musical tastes and preferences over time.
## Using the Spotify API
The available list of endpoints can be found here: <a href="https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-album">endpoints</a>
In order to get access to the spotify api, you need to follow the following steps:
* Go to the Developers site: https://developer.spotify.com/dashboard/applications, create an app and copy the client id and the client secret.
* The client id and client secret will be used to access tokens and refresh tokens. The access token will expire after each hour so we will need to generate a new one each time using the refresh token.


That's great! Creating a CI/CD pipeline for your Spotify Wrapped project using GitHub Actions is a good idea. Here's a general outline of what you can do:

Create a new GitHub repository to host your project, if you haven't done so already.
Write the necessary scripts to build and deploy your project. This can include scripts to install dependencies, perform database migrations, run tests, etc.
Create a workflow.yml file in the .github/workflows directory of your repository. This file defines the actions that should be taken when certain events occur (such as pushing to the main branch or creating a pull request).
Configure the GitHub Actions environment to match your project's dependencies and requirements. You can specify which version of Python, PostgreSQL, dbt, and other tools you want to use.
Test your pipeline locally by running the actions locally with act.
Push your changes to GitHub and watch as your pipeline runs automatically in response to new code changes.
There are many details to consider when setting up a CI/CD pipeline, such as secrets management, artifacts, and notifications. However, the steps above should give you a good starting point.

# I will define a simple workflow using Super-Linter. The end goal of this tool is:
# * Prevent broken code from being uploaded to the default branch
# * Help establish best practices across multiple languages
# * Build guidelines for code layout and format
# * Automate the process to help streamline code reviews

# For more information: https://github.com/marketplace/actions/super-linter
