def datadict():
    defs = ''' Data Dictionary:
    customer_id:
        The identification number of any client in the telco dataset.
    gender:
        The identified gender of any customer in the telco dataset.
        listed in english as 'Male' or 'Female.'
    senior_citizen:
        The status of a customer as a senior citizen in binary value.
        0: Not a senior
        1: senior citizen.
    partner:
        Status of whether or not a customer has a domestic partner.
        listed in Yes/No values.
    dependents:
        Status of whether or not a customer has dependents.
        listed in Yes/No values.
    tenure:
        How long the customer has been with the company in months
    phone_service:
        Status of whether or not the customer has phone service
        Yes/No values
    multiple_lines:
        Status of whether or not customer has multiple phone lines.
        Lists 'no phone service' if phone_service value is 'No'
    internet_service_type:
        Indication of what type of internet service customer has.
        DSL, Fiber, or no internet.
    internet_service_type_id:
        value by number of what type of internet service customer has.
        1: DSL
        2: Fiber
        3: No service
        ~~after remapping (int_type_id:)
        0: No service
        1:DSL
        2: Fiber
    online_security:
        Status of whether or not customer has online security service enabled.
        Yes/No
    online_backup:
        Status of whether or not customer has online backup services.
        Yes/No
    device_protection:
        Status of whether or not customer has device protection service.
        Yes/No
    tech_support:
        Status of whether or not customer has tech_support service.
        Yes/No
    streaming_tv:
        Status of whether or not customer has streaming television services
        Yes/No
    streaming_movies:
        Status of whether or not customer has streaming movie services.
        Yes/No
    contract_type:
        Type of contract customner is utilizing service on.
        month-to-month, one-year contract, or two-year contract.
    contract_type_id:
        Numeral represending what type of contract a customer is on
        0: month-to-month
        1: one-year contract
        2: two-year contract
    paperless_billing:
        Status of whether or not customer is enrolled in paperless billing.
        Yes/No.
    payment_type:
        What type of method a customer uses to pay for service.
        Electronic Check, Mailed Check, Automatic Bank Transfer, 
        or Automatic Credit Card Payment.
    payment_type_id:
        Numeral value indicating what type of payment type customer utilizes.
        1: Electronic Cheque
        2: Mailed Cheque
        3: Automatic Bank Transfer
        4: Automatic Credit Card Payment
    monthly_charges:
        Current amount in USD what customer is paying for services by month
    total_charges:
        Total amount customer has payed thus far in accrued monthly bills
        and/or charges
    churn:
        Whether or not a customer has churned, or in lamens terms, 
        left the company and discontinued service.
        Represented as Yes/No inititally, altered to:
        0: Not Churned
        1: Churned
    phone_id:
        Combination of phone service status and multiple phone line status.
        0: No service
        1: One line
        2: 2 or more lines
    household_type_id:
        Combination of partner and dependent status.
        0: No partner or dependents
        1: Partner with no dependents
        2: Dependent but no partner
        3: partner and dependent(s)
    streaming_services:
        Combination of streaming movie and streaming tv services.
        0: No streaming service
        1: Streaming 
        2: Streaming
        3: Both streaming services
    online_security_backup:
        Combination of online security and backup services
        0: No online Security or Backup Services
        1: Backup service with no Online Security
        2: Online Security but no Backup
        3: Both Security and Backup Services
    gender_e:
        enumerated version of gender column.
        0: Female
        1: Male

    device_protection_e:
        Enumerated version of device protection service.
        0: No device protection
        1: Device protection

    tech_support_e:
        Enumerated version of tech support services
        0: No tech support service
        1: tech support service

    paperless_billing_e:
        Enumerated version of paperless billing category.
        0: Not enrolled in paperless
        1: enrolled in paperless'''
    print(defs)