# Editing the Technical Specifications

## About this Guide

The description here applies to the [Data Exchange protocol](https://github.com/wbcsd/data-exchange-protocol) repository but is not limited to it whatsoever. 

## Tooling

The Tech Specs are written using [Bikeshed](https://speced.github.io/bikeshed/) which takes inspiration from Markdown and enriches it with additional features helpful for writing specification documents.

For diagrams, Mermaid is being used.

## Editing Markdown 
Editing can be done either online through GitHub or locally with tools like Microsoft Visual Studio Code, or any other text editor.

## Local Editing

To edit the specifications localy, you need to have [Python 3.x]([python.org]) and [NodeJs](nodejs.org) installed.

1. Install Bikeshed and Python Invoke

    ```
    pip3 install bikeshed
    pip3 install invoke
    ```

2. Install Mermaid

    ```
    npm install mermaid
    ```

Now you can build the documentation with 
> invoke clean build 

Which invokes the build instructions in `tasks.py`

## Statuses and Lifecycle

A Tech Specs document starts in the **Draft** status until it becomes a **Release.**. 

**Draft**

Such a document can and is supposed to be updated all the time (it is a “living document” in this sense) by the team of editors. 

The indented audience for a Draft document are editors and people immediately involved in the standard-setting process.

In case of the `data-exchange-protocol` repository, the resulting draft HTML is made available here:

[Technical Specifications for PCF Data Exchange (v3)](https://wbcsd.github.io/data-exchange-protocol/v/)

**Consultation Release**

A release made for consultation purposes, before an “actual” Release is made. This is typically a broader group of people than the ones regularly contributing to the tech specs.

**Release**

This means the document is fixed in terms of content and is not supposed to be updated any more. A release is made for everyone who is interested (i.e. beyond editors and the ones that are closely collaborated with).

Such a document is supposed to end up in the `tr` repo as a copy as well.

Once a release is made, the version number (see below for details) is taken, and each additional change to the document will result in the assignment of a new / different version.

All editing of a document therefore always happens against a **Draft** version


## Version Numbers

Whenever a (tech specs) document is released, its version number needs to be updated.

Within PACT, [Semantic Versioning](https://semver.org/)
is being used. Version numbers are constructied as *major*.*minor*.*patch*. Whenever a change breaks backwards-compatibility, a new major release must be created, e.g. from **1.1.3** to **2.0.0**.

Whenever a new feature or new functionality is added to the tech specs, a Minor Version Release will be created (e.g. **2.0.0** to **2.1.0**). 

All other small changes (fixes, remarks) should be a Patch Version Release (e.g. **2.1.0** to **2.1.1**)

In contrast to Releases, documents in Draft and Consultation state also have a timestamp appended to it:

the format is `$VERSION$-$YEAR$$MONTH$$DAY$`

Example: `2.0.0-20240309` (i.e. version `2.0.0` released May 9th of 2024)

## Change Categorization

There are at least 3 categories of changes which require different processes and handling by the editing team as well as the community

**Bug fix / Minor correction**

Within a Draft document wording, spelling mistake, inconsistencies, or other clarifying  have been detected and a fix was proposed. 
This is the “lowest” and least-effort category of changes. This change typically does not trigger the creation of a new release.

**Regular Editing**

A decision within the community was made and the resulting changes need to be applied to the tech specs. This usually comprises not “just” bug fixes but typically changes resulting from consensus with other community members. This is a category of change where the changes are especially (but not necessarily) made by the editing team.
In general, this type of change should be limited to cases where consensus and alignment with the community is absolutely clear, and that incorporating the changes are material to the tech specs in a broader sense.
This change might trigger a new release but must not necessarily do so.

**ADR Edits**

The “high effort” category of changes where community members actively engaged with and are material to the tech specs. 
This could be a new feature is added (or removed), backwards-breaking changes are introduced, etc. – i.e. a kind of change which at least results in a change in the minor, if not major, number of the version.
In most cases a new release is triggered (sometimes other ADRs are supposed to be integrated first, hence a release is not made immediately necessarily)

## Editing Process per Change Category

We distinguish between the 3 categories of changes as they require different editing processes

### **Bug fix / Minor correction**

**Process**

1 person makes the change and a second editing person reviews and acknowledges the change.

**Input**

A pull request by the party preparing the change with all the necessary tech specs changes (including collaterals) in it

**Output**

The pull request is merged. 

**Outcome**

A draft document is updated accordingly

### Regular Editing

**Process**

1 person makes the change.

A second editing person reviews and acknowledges the change.

If other community members are involved before or during the creation of the change, the authorative person(s) should be involved in the process as a reviewer as well

**Input**

A pull request by the party preparing the change with all the necessary tech specs changes (including collaterals) in it

**Output**

The pull request is merged. 

**Outcome**

A draft document is updated accordingly

If needed, the version number of the draft document is updated

### ADR Edit

**Process**

1 or more persons make the change, typically involving a community member who is not an editor already.

Community members are reviewing the change

The ADR reviewing process is announced and there is a deadline to provide feedback.

After the reviewing period, the ADR is decided upon. 

**Input**

A pull request by the party preparing the change with all the necessary tech specs changes (including collaterals) in it

**Output**

The pull request is merged after community consensus was reached.

**Outcome**

The draft document is updated accordingly.

If this hasn’t happened already compared with the latest release, the version number of the draft document is updated according to Semantic Versioning.

## Updating the Changelog

The summary of each change should be summarized and added to the changelog.

The changelog exists for regular readers to become up-to-date with latest changes to the tech specs. Changelog entries should not motivate changes (if this is required, probably an ADR is necessary then as well, in which case the ADR would explain the context and hence there would be no need to redundantly document the ADR in the tech specs as well) but only descriptive and should stay at a very high level.

The context and sections which were changed, should be linked to in the change log as well.

## Publishing

Anytime a commit is made on the main branch, GitHub will automatically build the updated HTML and diagrams. See the `.github/workflows` directory. 

This latest version will be published on https://docs.carbon-transparency.org/v3/

## Checklist before publishing

Make sure your `specs/v#/index.bs` file is ready. Follow this checklist:
 - Add an entry to to Changelog indicating that a release is being made, and whether it is a consultation draft or a stable version.
 - At the top of the file: set the text macro `STATUS` to either `Draft`, `Consultation` or `Release`
 - Set the publication date: `DATE yyyymmdd` 
 - Update version `VERSION major.minor.patch`
 - Update the `Previous Version` and `TR` links

Commit your changes with `git` and push to GitHub. The new version will automatically be built and published on https://docs.carbon-transparency.org/v3/

## Creating a release

Follow the checklist above (before publishing).
Make sure you don't have any uncommitted changes in your directory.

On your command line, navigate to the `data-exchange-protocol` directory.

Use the following command to create the release:
```
involke release
```
This will create all the artifacts and copy them to a new branch under the  `tr` directory.

Now navigate to the `../tr` directory and add + commit all changes.


Open a PR in the [`wbcsd/tr`](https://github.com/wbcsd/tr) Repository

On your browser, navigate to the [`wbcsd/tr`](https://github.com/wbcsd/tr) repository.

At the top of the page, you shall see a yellow box and a green button to open a Pull Request.

Click the green button "Compare & pull request". On the new page, scroll down and click the green button "Create pull request."

Merge the PR

Once you are ready (e.g., someone else from the team has reviewed it), merge the PR by clicking the green "Merge pull request" button.
