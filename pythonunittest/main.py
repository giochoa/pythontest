def stuff(num):
    try:
        if num:
            return int(num) +5
        else:
            return 'Please a number here'    
    except ValueError as err:
        return err   