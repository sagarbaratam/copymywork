
---
- hosts: host01

    become: true

    tasks:
      - name: output manipulation
        shell: "ls -lrt"
        register: "text"

      - debug:
          msg: "{{ text.stdout|regex_search(r'^out',multiline=True, ignorecase=True)}}"