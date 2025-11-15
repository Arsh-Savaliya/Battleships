#ifndef STRUCTS_H   
#define STRUCTS_H

struct transaction {
    int acc;     // which account to chose for transaction
    char type[12];   // type of transaction food/entertainment/education...
    char description[15]; // 1 word description of transaction
    float amt;   // amt to be deducted or recieved according to sign
    char date[15]; // DD-MM-YYYY
    struct transaction *next;
};

struct user{
    char accName[20];  // user name of a account
    int accID;  // account ID
    float balance;  // balance of a account
};

struct limits{
    float monthly;
    float yearly;
    float goal;
};

#endif
