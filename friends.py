mylist = [
        {"name": "Rachel", "job": "buyer", "traits": ["smart", "driven", "commercial", "fun"]},
        {"name": "Monica", "job": "doctor", "traits": ["driven", "silly"]},
        {"name": "Phoebe", "job": "actuary", "traits": ["crazy", "hardworking"]},
        {"name": "Joey", "job": "journalist",  "traits": ["moronic", "sexist", "lazy"]},
        {"name": "Chandler", "job": "accountant", "traits": ["funny", "sarcastic", "insecure"]},
        {"name": "Ross", "job": "lawyer", "traits": ["clever", "dorkey", "geeky"]}
        ]
for friends in mylist: 
    for trait in friends["traits"]:
        print(friends["name"] + " is " + trait)
