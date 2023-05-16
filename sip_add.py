import os
import yaml

new_configs = 0
base_dir = 'your/absolute/path/here'
def check_info(phone, last):
    try:
        phone = int(phone)
    except ValueError: # enforces only numbers are entered
        print('Phone number must be only numbers without spaces, dashes, or symbols try again.')
        print(f'Customer {last} NOT ADDED Please correct number in yaml file')
        print(f'Script ran with {new_configs} new customers added')
        exit()
    if len(str(phone)) != 10: # ensures the correct length
        print('Phone number must include area code and be exactly 10 digits')
        print(f'Customer \'{last}\' NOT ADDED Please correct number in yaml file')
        print(f'Script ran with {new_configs} new customers added')
        exit()

def make_files(last):
    sip_dir = f'{base_dir}/{last}'
    #uid = 1000 # find out and change
    #gid = 1000
    if not os.path.exists(sip_dir):
        os.makedirs(f'{sip_dir}')
        os.mknod(f'{sip_dir}/sip.conf')
        os.mknod(f'{sip_dir}/extensions.conf')
        #os.chown(sip_dir, uid, gid)
        return sip_dir
    else:
        return None

def build_config(sip_dir, last, phone, secret):
    # create sip.conf from template
    with open(f'template_sip.conf', 'r') as sip_file:
        sip_template = sip_file.read()
    sip_template = sip_template.replace('^', last)
    sip_template = sip_template.replace('!', str(phone))
    sip_template = sip_template.replace('#', secret)
    with open(f'{sip_dir}/sip.conf', 'w') as customer_sip_file:
        customer_sip_file.write(sip_template)
    
    # create extensions.conf from template
    with open(f'template_extensions.conf', 'r') as extensions_file:
        extensions_template = extensions_file.read()
    extensions_template = extensions_template.replace('^', last)
    extensions_template = extensions_template.replace('!', str(phone))
    extensions_template = extensions_template.replace('#', secret)
    with open(f'{sip_dir}/extensions.conf', 'w') as customer_extensions_file:
        customer_extensions_file.write(extensions_template)

def create_config(last, phone, secret):
    check_info(phone, last) # will not create config for invalid phone number or name
    sip_dir = make_files(last)
    if sip_dir is not None:
        build_config(sip_dir, last, phone, secret)
        return True
    return False

with open('sip_customers.yaml', 'r') as customer_file:
    customers = yaml.safe_load(customer_file)
CUSTOMERS = customers['customers']
for customer in CUSTOMERS:
    created = create_config(customer['last'], customer['phone'], customer['secret'])
    if created:
        new_configs +=1
print(f'Script ran with {new_configs} new customers added')
