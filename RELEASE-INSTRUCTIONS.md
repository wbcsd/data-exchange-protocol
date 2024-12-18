# Release Instructions

Follow the instructions below to trigger a release of the Technical Specifications.

> To trigger a release, you need to have sufficient permissions on the `wbcsd` GitHub organization, as well as on this (`wbcsd/data-exchange-protocol`) repository and in the target repository [`wbcsd/tr`](https://github.com/wbcsd/tr).

> You also need to have the GitHub CLI tool locally installed and be logged in to GitHub from your local terminal. See https://cli.github.com/ for further information.

## 1. Preparation

Make sure your `specs/v#/index.bs` file is ready. Follow this checklist:
 - Add an entry to to Changelog indicating that a release is being made, and whether it is a consultation draft or a stable version.
 - At the top of the file: set the text macro `STATUS` to either `Consultation` or `Release`
 - Set the publication date: `DATE yyyymmdd` 
 - Update version `VERSION major.minor.patch`
 - Update the `Previous Version` and `TR` links

## 2. Create the Release

On your command line, navigate to the `data-exchange-protocol` directory.

Use the following command to create the release:
```
make release
```
This will create the artifacts and copy them to a new branch under the  `tr` directory.

Now navigate to the `../tr` directory and add + commit all changes.

## 3. Open a PR in the [`wbcsd/tr`](https://github.com/wbcsd/tr) Repository

On your browser, navigate to the [`wbcsd/tr`](https://github.com/wbcsd/tr) repository.

At the top of the page, you shall see a yellow box and a green button to open a Pull Request.

Click the green button "Compare & pull request". On the new page, scroll down and click the green button "Create pull request."

## 4. Merge the PR

Once you are ready (e.g., someone else from the team has reviewed it), merge the PR by clicking the green "Merge pull request" button.
