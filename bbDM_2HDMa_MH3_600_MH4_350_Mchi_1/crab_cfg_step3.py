from CRABClient.UserUtilities import config
config = config()

config.section_("General")
config.General.transferLogs = True
config.General.requestName = 'EXO-bbDM_2HDMa_LO_5f_Ma10_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV'
config.General.workArea = 'crab_projects_step3'


config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.psetName = 'step1_PAT.py'
#config.JobType.maxMemoryMB = 10000


config.section_("Data")
config.Data.splitting       = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outputDatasetTag = 'EXO-bbDM_2HDMa_LO_5f_Ma10_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_TuneCP3_13TeV'
config.Data.inputDBS = 'phys03'
config.Data.outLFNDirBase = '/store/user/ptiwari/t3store2/2016_SignalSample_23102019/'
config.Data.publication = True
#config.Data.inputDataset = '/CRAB_PrivateMC/dekumar-EXO-sinp_0p35_tanb_1p0_mXd_10_MH3_600_MH4_150_MH2_600_MHC_600_step2-871705712505634bb6e8bf8a7788e376/USER'
config.Data.inputDataset = '/CRAB_PrivateMC/ptiwari-EXO-bbDM_2HDMa_LO_5f_Ma350_MChi1_MA600_tanb35_sint_0p7_MH_600_MHC_600_13TeV_step2-871705712505634bb6e8bf8a7788e376/USER'


config.section_("Site")
config.Site.storageSite = 'T2_IN_TIFR'
