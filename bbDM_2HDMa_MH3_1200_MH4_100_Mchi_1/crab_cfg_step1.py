from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.transferLogs = True
config.General.requestName = 'EXO-bbDM_2HDMa_LO_5f_Ma100_MChi1_MA1200_tanb35_sint_0p7_MH_600_MHC_600_13TeV_step1'
config.General.workArea = 'crab_projects_step1'


config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName = 'step1_DIGIPREMIX_S2_DATAMIX_L1_DIGI2RAW_HLT.py'
config.JobType.maxMemoryMB = 3500
#config.JobType.numCores = 8


config.section_("Data")
config.Data.splitting       = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.outputDatasetTag = 'EXO-sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_step1'
config.Data.outputDatasetTag = 'EXO-bbDM_2HDMa_LO_5f_Ma100_MChi1_MA1200_tanb35_sint_0p7_MH_600_MHC_600_13TeV_step1'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/ptiwari/t3store2/2016_SignalSample_23102019/'
config.Data.publication = True
config.Data.inputDataset = '/CRAB_PrivateMC/ptiwari-EXO-bbDM_2HDMa_LO_5f_Ma100_MChi1_MA1200_tanb35_sint_0p7_MH_600_MHC_600_13TeV_RAWSIMoutput-e159887c4196a923ae817a4fd243c0f0/USER'


config.section_("Site")
config.Site.storageSite = 'T2_IN_TIFR'
