from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.transferLogs = True
config.General.requestName = 'EXO-bbDM_2HDMa_LO_5f_Ma150_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV_step2'
config.General.workArea = 'crab_projects_step2'


config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName = 'step2_RAW2DIGI_RECO_EI.py'
#config.JobType.maxMemoryMB = 10000


config.section_("Data")
config.Data.splitting       = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'EXO-bbDM_2HDMa_LO_5f_Ma150_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV_step2'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/ptiwari/t3store2/2016_SignalSample_23102019/'
config.Data.publication = True
config.Data.inputDataset = '/CRAB_PrivateMC/ptiwari-EXO-bbDM_2HDMa_LO_5f_Ma350_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV_step1-80ebd718d73166d62c858a932af84443/USER'


config.section_("Site")
config.Site.storageSite = 'T2_IN_TIFR'
