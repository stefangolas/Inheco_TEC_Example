# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:12:47 2022

@author: stefa
"""
import os
from pyhamilton import (HamiltonInterface,  LayoutManager, 
 Plate96, Tip96, initialize, tip_pick_up, tip_eject, 
 aspirate, dispense,  oemerr, resource_list_with_prefix, normal_logging,
 layout_item, initialize_tec, set_target_tec, start_control_tec, stop_control_tec,
 terminate_tec)


lmgr = LayoutManager('deck.lay')


if __name__ == '__main__': 
    with HamiltonInterface(simulate=True) as ham_int:
        normal_logging(ham_int, os.getcwd())
        initialize(ham_int)
        initialize_tec(ham_int, controller_id = 0, simulating = True)
        set_target_tec(ham_int, target_temp=30, controller_id=0, device_id=1)
        start_control_tec(ham_int, controller_id=0, device_id=1)
        stop_control_tec(ham_int, controller_id=0, device_id=1)
        terminate_tec(ham_int, stop_all_devices=1)