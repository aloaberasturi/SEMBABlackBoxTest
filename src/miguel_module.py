#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.CMP import CMP, cmplog
from src.Lauchter import 
from src.TestList import TestList

TestList_1 = TestList().readFromDirectory("~/....../test_v2.0")
TestList_1 = TestList_1.filterByKey(["PW","SGBC",""])
TestList_1 = TestList_1.filterBySize(size=1000)

TestList_2omp    = UGRFDTDLauncherOMP (dest="~/....../test_v3.0_omp")
TestList_2mpi_12 = UGRFDTDLauncherMPI (dest="~/....../test_v3.0_mpi_12",n=12)

log1 = cmplog()
log1 = CMP(TestList_1, TestList_2omp, savelog=True, printscreen=True)
print(log1)
log12.save(dest="~/....../cmp_v2.0_vs_v3.0_OMP")
log1.Getstatistic()-> genera un histograma 

log12 = cmplog()
log12 = CMP(TestList_12, TestList_2mpi_12, savelog=True, printscreen=True)
print(log12)
log12.save(dest="~/....../cmp_v2.0_vs_v3.0_mpi_12")

logSelf = cmplog()
logSelf = CMP(TestList_2omp, TestList_2mpi_12, savelog=True, printscreen=True)
print(logSelf)
logSelf.save(dest="~/....../test_v3.0_self_mpi")
