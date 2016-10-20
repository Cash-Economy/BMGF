```money.days```

# Use-cases

## Assumptions:
- Users are existing savings group users
  - All savings group members are on the system
- System has access to:
  - Details from the User's bank accounts (all)
  - AND that the bank accounts reflect the majority of the income for the Users.
  - (We acknowledge that, since Users usually withdraw funds and hold them in cash, this would not be a good measure of expenses)

## Loop
*This product loop does not define the marketing or on-boarding of customers. Rather, it suggests the most common user flows.*

### Use-case 1 - User receives a cash injection
1. User receives income in their checking account (cheque cashing or direct deposit)
2. System polls the checking account (periodically, not triggered by point 1.) *Plaid*
  1. System catalogues the change in cash *Database*
  2. System compares this income injection to previous time-periods *at first statistics, then machine learning*
3. System notifies the User *Twilio*
  1. That they have received a cash deposit
  2. How this deposit compares to previous time periods
    1. Is this a usual periodic input?
    2. Is this a deviated month?
    3. Is this a windfall?
  3. That, due to the input, they have are incentivised to deposit funds into their money.days account via OR
    1. reminders of goal, and progress towards it
    2. points stimulus "deposit in the next day to receive [x] many bonus points"
    3. social stimulus "On average, your peers saved [x] amount when they received such an income boost"
    4. reminders of peer's goal and responsibility
4. User responds to the stimulus *Twilio or Web-App*
  1. With suggested deposit
    1. Which is then transacted *Plaid*
    2. Congratulations and confirmations are sent *Twilio*
  2. With greater than the suggested amount
    1. Which is then transacted *Plaid*
    2. Congratulations and confirmations are sent *Twilio*
  3. With lesser than the suggested amount
    1. Which is then transacted *Plaid*
    2. Congratulations and confirmations are sent, as well as progress towards minimum *Twilio*
  4. With no deposit
    1. Minor whinge sent reminding them of obligation *Twilio*
    2. If reccurrent *Database*
      1. Suggestion to speak to group administrator
5. Confirmation of order *Twilio*
6. Confirmation of transfer *Plaid and Twilio*
7. Update on points, progress and rank *Plaid*

### Use-Case 2 - Friend makes a transaction
1. User notified that friend has made a transaction *Twilio and Plaid*
2. User given the option to deposit (with point stimulus like point matching) *Twilio*
3. User responds *Twilio*
  1. With suggested deposit
    1. Which is then transacted *Plaid*
    2. Congratulations and confirmations are sent *Twilio*
  2. With greater than the suggested amount
    1. Which is then transacted *Plaid*
    2. Congratulations and confirmations are sent *Twilio*
  3. With lesser than the suggested amount
    1. Which is then transacted *Plaid*
    2. Congratulations and confirmations are sent, as well as progress towards minimum *Twilio*
  4. With no deposit
    1. Minor whinge sent reminding them of obligation *Twilio*
    2. If reccurrent *Database*
      1. Suggestion to speak to group administrator

# Use-Case 3 - non-transacting days
1. Reassuring text message sent *Twilio*
  1. You have x dollars and x points in the bank
  2. rank
  3. goal
  4. Progress
