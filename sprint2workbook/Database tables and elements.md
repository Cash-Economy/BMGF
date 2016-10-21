**Data Tables and Elements**:
- Users
  - User ID (primary key)
  - Username
  - First Name
  - Last Name
  - Preferred Name
  - Mobile phone number (string)
  - email address
  
- Groups
  - group id number (primary key)
  - group name
  - minimum deposit
  - frequency
  - opt-in to lottery? y/n
  
- User group membership
  - user ids + group id
  - membership type
  - date joined group

- Contribution Ledger
  - user id
  - group id
  - transaction time
  - transaction amount
  - lottery win  y/n
  - payout y/n
  - new balance
  
- Bank transaction Data
  - User ID
  - bank account/name
  - transaction time
  - transaction amount
  - transaction description
  
- User's Payment Methods
  - user id
  - bank account name
  - bank account type
  - bank account number
  
- User's points
  - user id + group id
  - date
  - previous point balance
  - points added/deleted
  - new points balance
  - transaction type
  
- User goals + monetary value
  - user id
  - goal name
  - goal amount
  
