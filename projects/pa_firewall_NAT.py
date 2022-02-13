nat_header = 'Name\t\tSource Zone\tDestination Zone\tDestination Interface\tSource Address\t\tDestination Address\tService\t\tSource Translation\tDestination Translation'
security_header = 'Name\t\t\tSource Zone\t\tSource Address\t\tDestination Zone\t\tDestination Address\t\tService\t\tAction\t\t'
example_nat_rule_1 = 'Winlogbeat\tLan\t\tLan\t\t\tEthernet1/10\t\t143.0.0.0/8\t\t143.0.0.150\t\twinlogbeat\tNone\t\t\tdestination-translation'
example_nat_rule_2 = '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAddress: 10.74.102.150'
example_nat_rule_3 = '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPort: 5044'
example_security_rule = 'Lan to SecOnion\t\tLan\t\t\t143.0.0.0/8\t\tNSM\t\t\t\t10.74.102.150\t\t\twinlogbeat\tAllow'
nat_s_translation = 'none'
nat_d_translation = 'destination-translation'
print('Hello! This is a pretty basic script designed to help you formulate NAT Rules and Security Rules to support those same NAT Rules for Palo Alto Firewalls! To get started, I will show you an example NAT Rule, and then allow you to enter information to help construct your own rules that you should be able to copy right into the Palo Alto Web Interface and be on your way!\n')
print('Example NAT Rules follows:')
print(nat_header)
print(example_nat_rule_1)
print(example_nat_rule_2)
print(example_nat_rule_3)
print('\nExample Security Rule in support of the above NAT Rule Follows:\n')
print(security_header)
print(example_security_rule)
print('\nThat was the tedious part! Now for the fun part!\n')
print("In order to set up a working NAT rule, there are questions I will need you to answer. I will use your input to construct the rule which you can then copy into a new NAT rule in the Palo Alto's Web UI\n")
nat_name = input('\n1. What do you want to name the NAT rule?\n')
nat_s_zone = input('\n2. In what Zone do those Ip address(es) reside?\n')
nat_d_zone = input('\n3. In what zone will the packet finally come to reside in?\n')
nat_d_interface = input('\n4. At which interface will the traffic enter the firewall at?\n')
nat_s_ip = input('\n5. What is the IP address(es) of the computer(s) initiating the connection?\n')
nat_d_ip =  input('\n6. What is the IP of the final destination the packet is going to?\n')
nat_service = input("\n7. What is the name of the service (DON'T FORGET TO SET UP A SERVICE OBJECT WITH YOUR DESIRED PORT(S)\n")
nat_d_translation_ip = input('\n8. What ip should the original public facing ip be replaced with?\n')
nat_d_translation_port = input('\n9. What port should the original public facing port be replaced with\n') 
print('You want your NAT rule to look like this:\n')
print(nat_header)
print(f'{nat_name}\t{nat_s_zone}\t\t{nat_d_zone}\t\t\t{nat_d_interface}\t\t{nat_s_ip}\t{nat_d_ip}\t\t{nat_service}\tNone\t\t\t{nat_d_translation}')
print(f'\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tAddress: {nat_d_translation_ip}')
print(f'\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPort: {nat_d_translation_port}')
print("Don't commit yet!\nYou also need a security rule to allow the NAT you just set up. This is where NAT can get little tricky, because of the way Palo Alto parses NAT rules and the associated security policies\n")
security_policy_name = input('\nWhat do you want to name the new security policy?\n')
security_d_zone = input('\nWhat is the final zone where your packet will rest after the above NAT rule is applied ?(i.e. What zone is the translated destination IP located in?\n')
print('\n')
print(security_header)
security_policy = f'{security_policy_name}\t\t{nat_s_zone}\t\t\t{nat_s_ip}\t{security_d_zone}\t\t\t\t{nat_d_translation_ip}\t\t\t{nat_service}\tAllow\n'
print(security_policy)
