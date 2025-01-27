# 44. Remove assurance flag

Date: 2024-12-11

## Context

In the current Tech Specs (2.x) the Assurance sub-record has a Boolean flag indicating whether or not assurance-related information is given:

```json
"pcf": {
	"assurance": {
		"assurance": true
		"coverage": "product level"
		"boundary": "cradle-to-gate"
		...
	}
}
```

This is superfluous: the presence of the `assurance` subrecord already indicates the inclusion of the assurance-related information, no boolean flag is necessary.

Moreover: setting the assurance attribute to `false` can lead to a confusing situation of setting the other attributes to `null` or empty strings, or omitting them.

## Proposal

Remove the`assurance` attribute and let the presence of an `assurance` sub-record indicate the availability of the information:

```json
"pcf": {
	"description": "PCF without assurance"
}
```

```json
"pcf": {
	"description": "PCF WITH assurance",
	"assurance": { 
	  "coverage": "product level"
		"boundary": "cradle-to-gate"
	}
}
```

## Consequences

As this would break backwards compatibility with version 2.x these changes should - if accepted - be included from version 3 upwards.

## Status

Presented in the Tech Working Group meeting of December 4, 2024. Feedback collected.

Call for consensus Dec 18, 2024.
Consensus reached.


