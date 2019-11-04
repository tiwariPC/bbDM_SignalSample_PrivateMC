from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import getUsernameFromSiteDB
config = Configuration()

workname = '2016_SignalSample'

config.section_("General")
config.General.transferLogs = True
config.General.requestName  = 'EXO-bbDM_2HDMa_LO_5f_Ma100_MChi1_MA1200_tanb35_sint_0p7_MH_600_MHC_600_13TeV'
config.section_("General")
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName  = 'PrivateMC'
config.JobType.psetName    = 'gensim_cfg.py'

config.JobType.disableAutomaticOutputCollection = False

config.section_("Data")
config.Data.splitting       = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits      = 200000
config.Data.outputDatasetTag = 'EXO-bbDM_2HDMa_LO_5f_Ma100_MChi1_MA1200_tanb35_sint_0p7_MH_600_MHC_600_13TeV'
config.Data.publication     = True
config.Data.outputPrimaryDataset = 'CRAB_PrivateMC'

config.section_("Site")
#config.Site.storageSite = 'T2_CH_CERN'
config.Site.storageSite = 'T2_IN_TIFR'
config.Site.whitelist = ['T2_*']
#config.Site.storageSite = 'T2_ES_IFCA'
#config.Site.whitelist = ['T2_ES_IFCA']
#config.Data.outLFNDirBase = '/store/user/%s/t3store2/%s' % (getUsernameFromSiteDB(), workname)
config.Data.outLFNDirBase = '/store/user/ptiwari/t3store2/2016_SignalSample_23102019'# %workname
