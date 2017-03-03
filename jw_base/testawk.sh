#!/usr/bin/env bash
#!/bin/awk -f

{
    if(NR==FNR)
        {a[$0]++}
    else
        {if($1 in a)
            print $0 >> "user_agence"
         else
            print $0 >> "user_no_agence"
        }
}