# Product Footprint Lifecycle # {#lifecycle}

## Introduction ## {#lifecycle-intro}

<div class=note>This section is non-normative</div>

The contents of a <{ProductFootprint|Product Footprints}> can change over time. For instance when a [=data owner=] publishes an updated Product Footprint ("upstream Product Footprints") which goes into the calculation of another Product Footprint ("downstream Product Footprint").

Even without upstream changes, a downstream Product Footprint can undergo changes in its own right, for instance when calculation errors are discovered and fixed, or when secondary emission databases are updated.

This section defines how changes to Product Footprints shall be handled by [=data owners=] and communicated to [=data recipients=] through the <{ProductFootprint}> data model.

For this, [=changes=] to ProductFootprint properties are defined and classified into [=minor change=] and [=major change=] ([[#lifecycle-classification]]). Depending on the change classification,

1. [=major changes=] must result in a new ProductFootprint ([[#lifecycle-major-changes]]) made available to its [=data recipients=],
1. [=minor changes=] result in either version updates ([[#lifecycle-minor-changes]]) or new ProductFootprint creation ([[#lifecycle-major-changes]])

In addition, if a Product Footprint is no longer valid, [=data owners=] can communicate this by applying a [=minor change=] through setting the <{ProductFootprint/status}> to `Deprecated`


## Change Definition and Classification ## {#lifecycle-classification}

A <dfn>change</dfn> to a <{ProductFootprint}> is defined as a change to one or more properties of a <{ProductFootprint}>, including a change of 1 or more properties from being undefined or to no longer being defined.

A <{ProductFootprint}> with <{ProductFootprint/status}> `Deprecated` MUST NOT be [=changed=].

There are 2 classes of changes to a <{ProductFootprint}>:

: <dfn>minor change</dfn>
::
    A [=minor change=] refers to a set of 1 or more [=changes=] to attributes to a <{ProductFootprint}>, including embedded data such as <{CarbonFootprint}>, etc.

    [=minor changes=] to a <{ProductFootprint}> SHOULD BE limited to correct errors, to incorporate changes in upstream data sources, or to incorporate changes in secondary data sources.

    A [=minor change=] is limited to the following <{CarbonFootprint}> properties:
      1. <{CarbonFootprint/pCfExcludingBiogenic}>, <{CarbonFootprint/pCfIncludingBiogenic}>,
         <{CarbonFootprint/fossilCarbonContent}>, <{CarbonFootprint/biogenicCarbonContent}>,
         <{CarbonFootprint/dLucGhgEmissions}>, <{CarbonFootprint/landManagementGhgEmissions}>,
         <{CarbonFootprint/otherBiogenicGhgEmissions}>, <{CarbonFootprint/iLucGhgEmissions}>,
         <{CarbonFootprint/biogenicCarbonWithdrawal}>, <{CarbonFootprint/aircraftGhgEmissions}>,
         <{CarbonFootprint/packagingEmissionsIncluded}>, <{CarbonFootprint/packagingGhgEmissions}>,
         <{CarbonFootprint/fossilGhgEmissions}>,
         <{CarbonFootprint/biogenicCarbonContent}>, <{CarbonFootprint/primaryDataShare}>,
         <{CarbonFootprint/secondaryEmissionFactorSources}>, <{CarbonFootprint/dqi}>,
         <{CarbonFootprint/primaryDataShare}> as a result of a change resulting from upstream ProductFootprints or an update to secondary data sources
      2. as a result of changes to the description properties
          <{CarbonFootprint/boundaryProcessesDescription}>, <{CarbonFootprint/allocationRulesDescription}>,
         <{CarbonFootprint/uncertaintyAssessmentDescription}>
      4. After a change to the assurance statement <{CarbonFootprint/assurance}> from being `undefined` to being defined

    A [=minor change=] MUST NOT change the <{ProductFootprint/id}> or the scope ([[#dt-carbonfootprint-scope]]) of the <{ProductFootprint}>.

: <dfn>major change</dfn>
::
    A [=major change=] refers to a set of 1 or more [=changes=] with 1 or more changes NOT conforming to the [=minor change=] definition.

    Additionally, a [=data owner=] CAN decide to handle a [=minor change=] as a [=major change=] (see [[#lifecycle-major-changes]] for further details).

<div class=example>
  Major change example: a [=data owner=] decides to publish Product Footprints with a sub-regional geographical granularity instead of a Product Footprint with scope `Global` ([[#dt-carbonfootprint-scope]]).

  The [=host system=] of the data owner then performs the following logical steps:

  1. deprecating the current Product Footprint ([[#lifecycle-minor-changes]]) by creating a new version with status set to `Deprecated`
  2. creating 1 or more new Product Footprints for each new geographical granularity ([[#lifecycle-major-changes]]),
  3. finally, making the new Product Footprints available to its [=data recipients=]

</div>

<div class=example>
  Minor change example: a [=data owner=] received an updated upstream Product Footprint which materially updates the <{CarbonFootprint/fossilGhgEmissions}> of one of its own Product Footprints.

  The [=host system=] of the data owner then performs the following logical steps:

  1. incorporating the <{CarbonFootprint/fossilGhgEmissions}> of the downstream Product Footprint into its Product Footprint
  2. creating a new version of the Product Footprint with the updated <{CarbonFootprint/fossilGhgEmissions}>
       by following the specification from [[#lifecycle-minor-changes]]
  3. finally, making the new Product Footprints available to its [=data recipients=]

</div>


## ProductFootprint version creation from minor changes ## {#lifecycle-minor-changes}

A [=minor change=] to a <{ProductFootprint}> MAY result in a new version of a <{ProductFootprint}>.

The [=data owner=] CAN represent a [=minor change=] to a <{ProductFootprint}> by creating 1 or more new <{ProductFootprint|ProductFootprints}> by following the specification from [[#lifecycle-major-changes]].

A version update to a <{ProductFootprint}> MUST be represented in the <{ProductFootprint}> by
1. incorporating the changes
2. incrementing <{ProductFootprint/version}> by 1 (or more)
3. setting <{ProductFootprint/updated}> to the time and date of the [=minor change=].
    If defined, <{ProductFootprint/updated}> MUST be strictly greater than the previous value of <{ProductFootprint/updated}>.
    Additionally, the value of <{ProductFootprint/updated}> MUST be strictly greater than the value of <{ProductFootprint/created}>.


## New ProductFootprint creation from major changes ## {#lifecycle-major-changes}

A [=Major change=] to 1 or more <{ProductFootprint|preceding ProductFootprints}> MUST result in

1. at least 1 new <{ProductFootprint}> being available to respective [=data recipients=]
2. for each of the preceding ProductFootprints, a new version being available to respective [=data recipients=] by
   1. following [[#lifecycle-minor-changes]]
   2. setting <{ProductFootprint/status}> to `Deprecated`

For each new ProductFootprint, the [=data owner=] MUST
1. make the necessary calculations for the new ProductFootprint
2. assign the new ProductFootprint a unique <{ProductFootprint/id}>
3. set <{ProductFootprint/updated}> to `undefined`
4. set <{ProductFootprint/precedingPfIds}> to the set of <{ProductFootprint/id}> of the 1 or more preceding ProductFootprints
