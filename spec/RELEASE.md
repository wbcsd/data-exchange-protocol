# Release Instructions

Follow the instructions below to trigger a release of the Technical Specifications.

> To trigger a release, you need to have sufficient permissions on the `wbcsd` GitHub organiztion, as well as on this (`wbcsd/data-exchange-protocol`) repositiory and in the target repository [`wbcsd/tr`](https://github.com/wbcsd/tr).

> You also need to have the GitHub CLI tool locally installed and be logged in to GitHub from your local terminal. See https://cli.github.com/ for further information.

## 1. Preparation

Make sure your `specs/v2/index.bs` file is ready. In particular, you should double check if:
- The version number (`Text Macro: VERSION <x.y.z>`) contains a date (e.g. `2.2.1-20240521`). This should only be used for the work in progress version of the Technical Specifications and should not be included in any release.
- There is a changelog entry, indicating that a release is being made, and whether it is a consultation draft or a stable version.

## 2. Trigger the Release Workflow

On your command line, navigate to the `data-exchange-protocol` directory.

Use the following command to trigger the release workflow from there:
```
gh workflow run release -f version=<x.y.z>
```
Make sure to replace `<x.y.z>` by the version of the Technical Specifications being released (e.g., `2.2.1`).

With the command above, the resulting Technical Specifications will be tagged as **Stable Release**.

If instead you wish to trigger a consultation draft, pass the `draft=true` input as follows:
```
gh workflow run release -f version=<x.y.z> -f draft=true
```
The resulting document will be tagged as **Consultation Draft**.

## 3. Open a PR in the [`wbcsd/tr`](https://github.com/wbcsd/tr) Repository

On your browser, navigate to the [`wbcsd/tr`](https://github.com/wbcsd/tr) repository.

At the top of the page, you shall see a yellow box and a green button to open a Pull Request, like the following:

<img width="920" alt="Screenshot 2024-05-21 at 19 20 01" src="https://github.com/wbcsd/data-exchange-protocol/assets/100690574/a3f6ee8e-d156-43df-b72d-fd961b3ebd50">

> Note that the branch name will include the date. This is intended and it does not mean that your version number is wrong. Note also that this screenshot is just an example.

Click the green button "Compare & pull request". On the new page, scroll down and click the green button "Create pull request."

<img width="935" alt="Screenshot 2024-05-21 at 19 20 30" src="https://github.com/wbcsd/data-exchange-protocol/assets/100690574/86fdbfba-2d88-4e3d-9036-6c2460e347d8">

## 4. Merge the PR

Once you are ready (e.g., someone else from the team has reviewed it), merge the PR by clicking the green "Merge pull request" button.

<img width="909" alt="Screenshot 2024-05-21 at 19 21 41" src="https://github.com/wbcsd/data-exchange-protocol/assets/100690574/befca359-1b1c-4c06-9435-e5cd07c50852">

