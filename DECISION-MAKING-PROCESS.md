# On providing feedback and participating in the development of the technical specifications

We welcome your feedback and participation in the development of the technical specifications.

For this, we use an ADR-inspired process.

To make a meaningful contribution:

## ADR Submission, Review, and Acceptance Process
Architecture decisions and changes to the technical specification are submitted via creating a ``Markdown``

- ADRs are numbered sequentially and monotonically. Numbers are not reused.
- Format of the ADR: Please see an [existing ADR](https://github.com/wbcsd/data-exchange-protocol/blob/adr-0021-auth-conformance-issues/decisions/log/0015-pagination.md) for the format

### Submitting an ADR

- Fork and Clone the repo to your local
- Create a new branch (name as you prefer but recommend to use your GitHub handle + "-" + adr name e.g. <githubhandle>-adr-0016)
- Create a Markdown file for the ADR under the [decisions/log](decisions/log/) folder in your local branch (based on the proposed format)
    -  If possible, submit respective changes (based on your ADR proposal) already to the technical specification text as well (see above)
- Commit and push the changes to github repo and raise a PR to merge the forked repo into WBCSD `base repo` (for more information please refer [this link](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)). Tag reviewers as necessary or communicate via email to the concerned audience to get the ADR Review process started

### Reviewing an ADR

- If you are tagged as a "Reviewer" in a PR submitted for an ADR proposal Or you are informed regarding a PR submitted for an ADR proposal, then please follow these steps
    - Open the concerned PR and navigate to the `Files changed` tab
    - Start your review of the proposed changes, and if you would like to provide feedback  - please use the GitHub "inline comments" feature
    - Once you have finished your review and added your feedback, please submit the Review as below -
        - If you have added inline comments as feedback then please select the   <img width="170" alt="image" src="https://github.com/wbcsd/data-exchange-protocol/assets/1404233/56a56487-ae01-46b1-9d63-dd8dd358afea"> option and "Submit Review"
        - If you didn't add any inline comments and are aligned on the proposed changes in the ADR then select the   <img width="170" alt="image" src="https://github.com/wbcsd/data-exchange-protocol/assets/1404233/631fb928-b960-40d2-b0b5-4e81dce8ad0b"> option and "Submit Review"

 ### Process for Accepting feedback

- Reviewers will review and provide their feedback as depicted above
- Incorporate the comments as applicable or reply via inline comments as necessary
- Once there is consensus on the ADR proposal, update the Status of the ADR to “Accepted". PACT Team will then merge the ADR proposal into the `main` branch

## Propagating Accepted ADR changes to Technical Specification
- Content from Accepted ADRs will be incorporated in the applicable Technical Specification as below -
    - If the PR for the ADR **did not already include** proposed changes to the Technical Spectification ([see above](https://github.com/wbcsd/data-exchange-protocol/edit/main/README.md#on-providing-feedback-and-participating-in-the-development-of-the-technical-specifications:~:text=If%20possible%2C%20submit%20respective%20changes%20(based%20on%20your%20ADR%20proposal)%20already%20to%20the%20technical%20specification%20text%20as%20well%20(see%20above))) and was merged into `main` branch -  then a new PR needs to be submitted with the respective changes. Otherwise if the PR was not merged into the `main` branch, please Commit the respective changes in the same PR. <br/><br/>
    > **_NOTE:_** The PR for Technical Specificaiton related changes only, will be reviewed and merged (if accepted) into `main` branch by the PACT Team

    - If the PR for the ADR **already included** the proposed changes to the Technical Spectification, then no additonal PR is needed and the changes will be merged in `main` branch



## History of decisions

Accepted decisions are stored in the directory [decisions/log](decisions/log/) under branch `main`.
