#Architecture Diagram

> ### Narrative
> How might we formalize informal savings pools to make them more useful for their members?
> See [Story Board](https://github.com/Cash-Economy/BMGF/blob/master/Artifacts/elements/storyboard/Storyboard%20v1.jpg)

## Scaffolding (open source reuse, core technology)
![Architecture Diagram](https://github.com/Cash-Economy/BMGF/blob/master/Artifacts/elements/architecture-diagram/architecture%20diagram%20v1.jpeg "Version 1 of Architecture Diagram")

## Ratholes:
- Trying to define each and every potential business logic of the system (avoid by relying on self-selection)
    - This requires too many assumptions about user preferences
    - This assumes a singular set of preferences across user groups
- Trying to design higher-level analytics functionality (see dependency)
- Rulemaking and savings pool governance
    - We don’t have sufficient data about the explicit and implicit rules by which savings groups are governed
    - Different groups may have different governance norms; the degree of variance here will determine how flexible the rulemaking feature should be
- Trying to solve multiple use cases
    - There can be many potential benefits to formalizing informal savings pools, however, the core premise that users will adopt a formal structure for savings groups needs to be validated
    - As a hypothesis, we will focus on a single use case: emergency disbursements from the savings pool to smoothen income shocks to a single member

## Dependencies:
- Higher-level analytics depend on having collected data from multiple user groups
    - Avoid this rathole
- Lack of real user data
    - Use dummy data based on [initial research findings](https://github.com/Cash-Economy/BMGF/tree/master/research/savings-groups-data)
- Rules and governance
    - Identify one loosely defined set of governance rules for prototype
    - Single-leader model, core functionality (use case) will be for emergency disbursements
- Emergency disbursements use case
    - Take ordered disbursements as a given
    - Use fixed value as a percentage, based on initial research findings

## Core technology:
- Ledger system and interface
    - How will pay-ins and pay-outs be recorded in the system
    - What information will be displayed to each type of user (leader vs. group members) through the interface
    - Sample business logic (back end) to capture use case of emergency disbursements
