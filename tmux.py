#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

from ansible.module_utils.basic import AnsibleModule
from os import system
from datetime import datetime

def run_module():
    d1 = datetime.now()
    d1 = str(d1.day) + "-" + str(d1.month) + "-" + str(d1.year) + "-" + str(d1.hour) + "-" + str(d1.minute) + "-" + str(d1.second)


    # define the available arguments/parameters that a user can pass to
    # the module
    module_args = dict(
        cmd=dict(type='str', required=True),
        name=dict(type='str', required=False, default=d1)
    )

    module = AnsibleModule(
        argument_spec=module_args
    )
    

    # create a tmux session (giving it a name so we can send it a command)
    system('tmux new-session -d -s %s' % module.params['name'])
    
    # send the tmux session the command we want to execute on it
    system('tmux send -t %s "%s" ENTER' % (module.params['name'], module.params['cmd']))

    result = dict(
        message='New tmux session created with name: %s' %module.params['name']
    )

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
