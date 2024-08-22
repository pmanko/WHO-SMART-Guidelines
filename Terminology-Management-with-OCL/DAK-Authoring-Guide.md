# To Dos

* Change headers to use more DAK author-like language (look at L2 SOP for examples)

# Setup and Prerequisites

1. An official OCL Organization should be created as the home for all WHO DAK content. In this example, it will be [WHO-SG-Example](https://app.staging.openconceptlab.org/#/orgs/WHO-SG-Example/sources/).
2. Developers of the DAK dictionary will have an OCL account in the appropriate OCL instance, and they have been added to the WHO organization as a member.
3. 

# Start up the DAK dictionary

An OCL source will serve as the primary home for DAK concepts, whether they will be represented as in the L3 FHIR resources as Profiles or Value Sets.

1. Use the Create Source button to pull up a form to fill in the details for the DAK.

   ![1723231674729](image/Terminology-Management-Guide/1723231674729.png)
2. Fill out required fields for this source, based on the DAK being developed.

   * Recommended Configurations for most DAKs:
     * Source Type: Dictionary
     * Validation Schema: TBD
     * Visibility: TBD (Private)
     * Canonical URL: TBD
     * FHIR Settings:
       * Purpose: [DAK one-word name]
       * **TBD:** Other common settings required e.g. Publisher?
   * Recommendation: To improve implementation of DAKs in OpenMRS instances, it is recommended that the OpenMRS Validation Schema is used, and External IDs in the "ID Auto-Assignment" section should all be set to "UUID" to give all concepts and names/descriptions a unique identifier.
     * **TBD:** Should the OpenMRS Validation Schema be used? It helps to reduce duplicate names within the DAK source, among other things that enhance implementability in OpenMRS.
   * **Note:** Sources will use the Purpose attribute as a way to tie DAK contents together, until resource packaging is supported in OCL.
3. It is recommended that preliminary descriptive information about the DAK is provided in the Source About page, if available. This is the place to describe in detail the intended use of the DAK, assumptions, and other important information about its contents. It is also an ideal place to link to the other artifacts, GitHub reposotories, etc. that are related to your DAK. This content can be added at any time but should be populated before releasing a version of the DAK in order to appear in your FHIR terminology resource(s).
4. Click "Create Source" to submit information and create the DAK source. Once the page refreshes, ensure that the Canonical URL of the source is visible and correct. Click on the Source to enter it and to view its contents.

# Creating Concepts in the DAK

Whether the data dictionary element represents a question, an answer, or something else, they all will be defined as concepts within the DAK source. We can give them different attributes to differentiate, and we can also add or manage mappings on concepts. These concepts can later be organized, enriched, or otherwise altered in the future, but we will focus on the initial creation of the concepts first.

Note that concepts should ideally be reused where possible, rather than created from scratch.

## Searching for and reusing concepts

Use the search bar at the top of the page to input keywords or other search terms that could help to find an existing concept that meets the need of the DAK dictionary that is being developed.

Using the search results provided, look for a concept that is similar to the requirement for the DAK dictionary. This includes a similar display name, description, Attributes, and Associations. Note that, particularly for question concepts, having some imperfect matching in the associations section can be acceptable since the mappings can be changed later.

In general, it is better to reuse a concept as long as the intended meaning of the concept matches the requirement. Consult the DAK management group for questions of similarity and appropriateness of reuse.

### $clone

OCL's cloning operation can recreate a concept and its mappings, making it easier to reuse (and possibly adapt) in the current DAK dictionary. When selecting one or more concepts in OCL, use the Clone to Source button to bring up a prompt that will enable you to preview and customize this operation to make copies of a concepts for your own dictionary.

Note that the clone operation by default will "cascade", meaning it will recreate both the concept and its mappings if those mappings are of a certain type. This operation can be customized to change how this cascade works.

### Visual example of searching and cloning

![1723829331016](image/DAK-Authoring-Guide/1723829331016.png)

### Making adaptations to a cloned concept

Various adaptations can be made to concepts:

* Add new names/synonyms/descriptions, change the preferred name for the locale, etc.
* Change mappings or associations
* Change Attributes

Use OCL's Edit Concept button in the Actions menu to make these changes.

Adding translations to this concept can also be done using this action by creating new names and assigning a different Locale code to them.

Note that IDs cannot be changed on any concept.

![1723831205307](image/DAK-Authoring-Guide/1723831205307.png)

### Questions and Discussions

* What is the order of preference of sources to search for concept reuse? Proposed order:
  * DAK Core Dictionary: Any concept can be reused verbatim or adapted (Note that any concepts from other DAK dictionaries should have a representation here, so no other DAK dictionaries should be required for searching unless they are in a pre-publication stage)
  * Reference Terminologies including ICD-10, ICD-11, SNOMED-GPS, LOINC, etc. (Note that these offer starting points but likely will need additional information to be usable for the DAK dictionary being developed)
  * CIEL? (Can simply be used as a reference for modeling the concepts, remaking a list of common answers to a question, etc.)
  * Other sources?
* Gap: $clone does not allow the user to manually input an ID - OCL instead autoassigns an ID. Should we support a WHO auto-ID schema, or perhaps should we change the clone operation to allow manual ID input?
* 

## Creating a Concept (e.g. a Data Element)

Click the "+" icon to "Add Concept". This will open the form to create a concept, which will contain the necessary fields to fill out for each data element.

![1723466584922](image/DAK-Authoring-Guide/1723466584922.gif)

Click the "Create" button to submit the concept to OCL. OCL may return errors if improper values are provided.

A visual example of populating the attributes for an OCL concept is shown below, using an example from the DAK Dictionary Template (**link to be added**):

![1723471361867](image/DAK-Authoring-Guide/1723471361867.gif)

See the Dictionary Checklist section for the required and optional attributes for concepts.

## Adding Mappings to a Concept

Any concept, whether they are data elements or input options, can have mappings, including the following:

* Internal mappings: Connect two concepts in the DAK dictionary
* External mappings: Link a DAK dictionary concept to an external vocabulary, such as ICD-10

OCL's Associations section within a concept's details page allows you to add a mapping from that concept to another concept. In general, **it is better to already know what concept you want to map to**, since this Add Mapping form is not ideal for searching for a concept. This may require opening up another OCL tab to search for concepts, or you may need to search for codes in another terminology's browser e.g. the ICD-10 Browser.

Once you know your concept that you want to map to, navigate to the concept's Associations section and use the "Add new mapping" option or the Three-dot menu of another mapping to open a form that will help you to create the new association between data element and input option(s). Select the applicable Map Type, then select the source (i.e. the dictionary or reference vocabulary) that will contain the concept to map to. If that source does not exist in OCL, contact the OCL administrator.

Then you can input the code or name of the concept to map to. If OCL does not recognize that code or name in the source, it will allow you to provide your own name to the concept. This ensures that you can still provide meaningful mappings to a concept that OCL does not recognize.

See below for visual examples of adding mappings to a concept.

**Check this:** This process should be used not only to map concept to reference vocabs, but also back to the Core DAK dictionary that will contain common concepts. If you cloned a Core DAK concept, however, then this step has likely already been done by OCL for you.

Adding a mapping to a concept that OCL recognizes:

![1724088612169](image/DAK-Authoring-Guide/1724088612169.png)

Adding a mapping to a concept that OCL does not recognize:

![1724095326750](image/DAK-Authoring-Guide/1724095326750.png)

## Creating input options for a coded data element

In the case that a new input option is needed for a coded data element (e.g. a new possible answer to a question concept), you first must create the concept in the DAK source, following the directions above. Searching for and reusing existing concepts is still preferable, but creating a new concept to serve as an input option will likely be needed at some point in the DAK development process.

Once all required input options for a coded data element have been created in the DAK source, open the details for the data element and navigate to the Associations section. Use the "Add new mapping" option or the Three-dot menu of another mapping to open a form that will help you to create the new association between data element and input option(s).

**TBD**: Which map type to use? (If at all?)

![1724088078334](image/DAK-Authoring-Guide/1724088078334.png)

# Creating a value set of input options

1. Select the concepts to be added (often in the DAK source)
2. Search for an existing value set to place the concepts into
   1. Create the value set, if not already existing.
      1. Ensure that the value set is being created in the appropriate Org, since OCL defaults to placing value sets in the User's ownership, and ownership is not easy to change.
      2. Note that not all details need to be filled in now.
3. OCL will display a dialogue to ask if a cascade should be used. In general, it is recommended to at least use the cascade option that says "Yes, include associated Mappings from the same source"
4. Recommended: link the value set back to the data element concept using the "Value Set URL" (and "Value Set Canonical") attribute(s) (URL = OCL URL, Canonical = Universal identifying URL)

Note that the example below is done using DAK concepts, although it is possible to follow the same workflow from another OCL source.

![1724269990687](image/DAK-Authoring-Guide/1724269990687.png)


# Managing repository versions

Save versions of all created repositories at the end of the development process when ready to share content for broader feedback.

# Dictionary Checklist

The following tables display the required and optional attributes to be present when developing terminology artifacts for DAK dictionaries. Some of these attributes are required to create something within OCL, but all attributes in the Required section will be needed to publish the completed DAK to the SMART Guidelines community.

## Concept Attributes

### Required

When creating concepts (data elements or input options), the following OCL fields should be populated (using these values from the DAK data dictionary if available):

| OCL Field                      | DAK Data Dictionary Attribute   | Example Value                                                             | Notes                                                                                                                                       |
| ------------------------------ | -------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Concept ID                     | Data element ID                  | ANC.B5.DE48                                                                | This ID value is permanent and cannot later be changed on a concept.                                                                        |
| Concept Class                  | "Data Element" or "Input Option" | Data Element                                                               | Other values may be permitted by WHO DAK community.                                                                                         |
| Datatype                       | Data type                        | TBD                                                                        | TBD                                                                                                                                         |
| (Names & Synonyms) Locale      | N/A                              | en                                                                         | Use whatever locale (i.e. language code) is applicable to the name                                                                          |
| (Names & Synonyms) Name       | Data element label               | ANC danger signs                                                           | Multiple names and synonyms can be added, each with their own Locale and Type                                                               |
| (Names & Synonyms) Type        | N/A                              | Fully-Specified                                                            | Describes which name type should apply to this concept name. Having at least one preferred fully specified name per locale is recommended. |
| (Names & Synonyms) External ID | N/A                              | N/A                                                                        | If the OCL source is configured properly, then OCL will automatically assign this value.                                                    |
| (Names & Synonyms) Preferred   | N/A                              | ✓                                                                         | Designates that the name is preferred within this locale                                                                                    |
| (Descriptions) Locale         | N/A                              | en                                                                         | Use whatever locale (i.e. language code) is applicable to the name                                                                          |
| (Descriptions) Name           | Description and definition       | "Indicates observations health worker made when checking for danger signs" | Multiple descriptions can be added, each with their own Locale and Type.                                                                    |
| (Descriptions) Type           | N/A                              | Definition                                                                 | Describes which type should apply to this concept description. Having at least one Definition per locale is recommended.                    |
| (Descriptions) External ID    | N/A                              | N/A                                                                        | If the OCL source is configured properly, then OCL will automatically assign this value.                                                    |
| (Descriptions) Preferred       | N/A                              | ✓                                                                         | Designates that the description is preferred within this locale                                                                             |

### Optional

Additionally, the following attributes from the DAK can be defined as Custom (AKA Extra) Attributes in OCL if applicable:

| DAK Attribute                                      | OCL Extra Attribute                  | Example Value                                                                                              |
| -------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Activity ID and name                               | Activity_ID_and_name                 | ANC.B5. Quick check                                                                                        |
| Quantity subtype                                   | Quantity_subtype                     | Integer quantity                                                                                           |
| Validation condition                               | Validation_condition                 | Must be a date and time value                                                                              |
| Optionality                                        | Optionality                          | R                                                                                                          |
| Explain conditionality                             | Explain_conditionality               | Required if client was tested for other specified STI (STI tested for [Data Element ID] = Other (specify)) |
| Functional grouping of data elements               | Functional_grouping_of_data_elements | Immunization event                                                                                         |
| Linkages to decision-support tables                | Linkages_to_decision_support_tables  | TBD                                                                                                        |
| Linkages to scheduling logic tables                | Linkages_to_scheduling_logic_tables  | TBD                                                                                                        |
| Linkages to aggregate indicators                   | Linkages_to_Aggregate_Indicators     | TBD                                                                                                        |
| Annotations                                        | Annotations                          | This field can also be calculated as defined by member states                                              |
| Intended FHIR Resource for profile (if available) | HL7_FHIR_R4_Resource                 | TBD                                                                                                        |

### Questions and Discussions

* Data type: Need to figure out how DAK values map to OCL values
* Name type: What is the OpenMRS requirement for this value? How are synonyms represented?
* Where should we be managing potential values for fields like "Optionality"? Should we make OCL value sets?
* Are any of these Extra Attributes required? What requirements or guidance are there? Or is it open ended for now?
* Please populate "TBD" values in Dictionary Checlist section

## DAK Dictionary (Source)

## Value Sets (Collections)

# Major TBDs, Gaps, and/or Assumptions

## Gaps and TBDs

* **ID Generation:** In the absence of DAK-specific ID generation, IDs will need to be assigned manually OR they will need to use a simple numeric ID that can be auto-generated.
* **Canonical URL Assignment:** Canonical URLs can be whatever URL we want them to be, so an official method should be decided and listed in the SOP.
* **Concept Properties:** In the absense of CodeSystem property support, all concept properties outside of OCL's data model will be stored as Extra attributes, including but not limited to the following properties: "Activity ID and name", "Quantity subtype", "Calculation", "Validation condition", "Optionality", "Explain conditionality", "Functional grouping of data elements", "Linkages to decision-support tables", "Linkages to scheduling logic tables", "Linkages to aggregate indicators", "Annotations", "Intended FHIR Resource for profile" (if available)
* **Packaging:** In the absence of packaging features for specific DAKs, there may need to be a way to group or retrieve OCL content that denotes what DAK(s) it should be packaged with. Example: Use the Purpose FHIR attribute of the CodeSystem, ValueSet, and ConceptMap resources
  * In the absence of downloading the appropriate FHIR resources, a script will be required that saves the individual FHIR resources from the WHO organization as files, which can be used for FHIR IG generation.
* **Source Visibility:** In the absence of features for advanced roles and permissions, the only security feature is to use Private repositories. WHO should have a stance on whether or not their in-draft DAK content should be visible outside of the members of OCL's WHO organization. This affects whether OCL repos are developed in Private or in Public (View Only) mode.
  * Suggestion: Develop in Private mode until there is need for broader feedback, then publish in View Only mode using a Draft (e.g. 0.1.0) version.
* **Map Types:** What are the preferred map types for the following scenarios? (Common OCL map types that work with OpenMRS include SAME-AS, Narrower-Than, Broader-Than, Q-AND-A, Concept-Set)
  * Adding an Input Option to a coded Data Element
  * Organizing concepts into a set or list
  * Mapping two concepts with the same meaning
  * Mapping a concept as inexactly mapped to another concept (e.g. narrower-than or broader-than)

## Assumptions

1. **Check this:** WHO will now allow DAK authors to create value sets that consist directly of reference vocabulary codes. They must instead DAK-specific concepts that act as the go-between for reference vocabulary codes.
2. Short-term Approach: Each DAK plus the Core dictionary exist as separate dictionaries, putting a layer of separation between concepts from different DAKs.

   1. Example: If a concept starts in Immz, it can also go to the Core dictionary with a mapping between the Immz and Core concepts.
   2. Pro: Separation of concepts is done intentionally; mapping can be done to link same-as concepts.
   3. Con: DAK Proliferation is harder to manage in long term; changes to concept(s) will need to be managed in multiple places: at the concept level AND at the mapping level; searching for and reusing concepts may be harder - which concept to reuse?
