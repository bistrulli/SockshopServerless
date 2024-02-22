import sys
sys.path.append('/Users/emilio-imt/git/MPP4Lqn')

from entity import *
from Lqn2MPP import Lqn2MPP
		
if __name__ == '__main__':
	
	lqn2mpp=Lqn2MPP()
	nusers=1
	
	T_SockClient=Task(name="T_SockClient",proc=Processor(name="T_SockClient",mult=nusers,sched="f"),tsize=nusers,ref=True)
	T_SSAddress=Task(name="T_SSAddress",proc=Processor(name="T_SSAddress",mult=nusers,sched="f"),tsize=nusers)
	T_SSHome=Task(name="T_SSHome",proc=Processor(name="T_SSHome",mult=nusers,sched="f"),tsize=nusers)
	T_SSCtlg=Task(name="T_SSCtlg",proc=Processor(name="T_SSCtlg",mult=nusers,sched="f"),tsize=nusers)
	T_SSCart=Task(name="T_SSCart",proc=Processor(name="T_SSCart",mult=nusers,sched="f"),tsize=nusers)
	T_SSList=Task(name="T_SSList",proc=Processor(name="T_SSList",mult=nusers,sched="f"),tsize=nusers)
	T_SSItem=Task(name="T_SSItem",proc=Processor(name="T_SSItem",mult=nusers,sched="f"),tsize=nusers)
	T_SSGet=Task(name="T_SSGet",proc=Processor(name="T_SSGet",mult=nusers,sched="f"),tsize=nusers)
	T_SSAdd=Task(name="T_SSAdd",proc=Processor(name="T_SSAdd",mult=nusers,sched="f"),tsize=nusers)
	T_SSDel=Task(name="T_SSDel",proc=Processor(name="T_SSDel",mult=nusers,sched="f"),tsize=nusers)
	T_SSCatQuery=Task(name="T_SSCatQuery",proc=Processor(name="T_SSCatQuery",mult=nusers,sched="f"),tsize=nusers)
	T_SSCartQuery=Task(name="T_SSCartQuery",proc=Processor(name="T_SSCartQuery",mult=nusers,sched="f"),tsize=nusers)
	
	SockClient = Entry("SockClient")
	T_SockClient.addEntry(SockClient)
	SSAddress = Entry("SSAddress")
	T_SSAddress.addEntry(SSAddress)
	SSHome = Entry("SSHome")
	T_SSHome.addEntry(SSHome)
	SSCtlg = Entry("SSCtlg")
	T_SSCtlg.addEntry(SSCtlg)
	SSCart = Entry("SSCart")
	T_SSCart.addEntry(SSCart)
	SSList = Entry("SSList")
	T_SSList.addEntry(SSList)
	SSItem = Entry("SSItem")
	T_SSItem.addEntry(SSItem)
	SSGet = Entry("SSGet")
	T_SSGet.addEntry(SSGet)
	SSAdd = Entry("SSAdd")
	T_SSAdd.addEntry(SSAdd)
	SSDel = Entry("SSDel")
	T_SSDel.addEntry(SSDel)
	SSCatQuery = Entry("SSCatQuery")
	T_SSCatQuery.addEntry(SSCatQuery)
	SSCartQuery = Entry("SSCartQuery")
	T_SSCartQuery.addEntry(SSCartQuery)
	
	
	
	###### SockClient logic
	
	###### SockClient activities and calls
	SockClientSockClient_a1=SynchCall(dest=SSAddress, parent=SockClient, name="SockClient_a1ToSSAddress")
	SockClient.getActivities().append(SockClientSockClient_a1)
	SockClientSockClient_a2=Activity(stime=1.0, parent=SockClient, name="SockClient_a2")
	SockClient.getActivities().append(SockClientSockClient_a2)

	###### SockClient Activity Diagram
	SockClientD0=probChoice(parent=SockClient, name="SockClientD0", 
									probs=["P_SockClientSockClient_a2SockClientD0"], 
									branches=[SockClientSockClient_a2], 
									origin=SockClientSockClient_a1)
	SockClient.getDnodes().append(SockClientD0)
	SockClientDf=probChoice(parent=SockClient, name="SockClientDf", 
									probs=["P_SockClient_a1"], 
									branches=[SockClientSockClient_a1], 
									origin=SockClientSockClient_a2)
	SockClient.getDnodes().append(SockClientDf)
	
	
	###### SSAddress logic
	
	###### SSAddress activities and calls
	SSAddressSSAddress_a1=Activity(stime=1.0E-4, parent=SSAddress, name="SSAddress_a1")
	SSAddress.getActivities().append(SSAddressSSAddress_a1)
	SSAddressSSAddress_SSHome=SynchCall(dest=SSHome, parent=SSAddress, name="SSAddress_SSHomeToSSHome")
	SSAddress.getActivities().append(SSAddressSSAddress_SSHome)
	SSAddressSSAddress_SSCtlg=SynchCall(dest=SSCtlg, parent=SSAddress, name="SSAddress_SSCtlgToSSCtlg")
	SSAddress.getActivities().append(SSAddressSSAddress_SSCtlg)
	SSAddressSSAddress_SSCarts=SynchCall(dest=SSCart, parent=SSAddress, name="SSAddress_SSCartsToSSCart")
	SSAddress.getActivities().append(SSAddressSSAddress_SSCarts)
	SSAddressSSAddress_work=Activity(stime=1.0, parent=SSAddress, name="SSAddress_work")
	SSAddress.getActivities().append(SSAddressSSAddress_work)

	###### SSAddress Activity Diagram
	# connect the entry to the main activity of function 
	SSAddressDI=probChoice(parent=SSAddress, name="SSAddressDI", 
									probs=["P_SSAddressSSAddress_a1"], 
									branches=[SSAddressSSAddress_a1], 
									origin=SSAddress)
	SSAddress.getDnodes().append(SSAddressDI)
	SSAddressD0=probChoice(parent=SSAddress, name="SSAddressD0", 
									probs=["P_SSAddressSSAddress_SSHomeSSAddressD0","P_SSAddressSSAddress_SSCtlgSSAddressD0","P_SSAddressSSAddress_SSCartsSSAddressD0"], 
									branches=[SSAddressSSAddress_SSHome,SSAddressSSAddress_SSCtlg,SSAddressSSAddress_SSCarts], 
									origin=SSAddressSSAddress_a1)
	SSAddress.getDnodes().append(SSAddressD0)
	SSAddressD1=probChoice(parent=SSAddress, name="SSAddressD1", 
									probs=["P_SSAddressSSAddress_workSSAddressD1"], 
									branches=[SSAddressSSAddress_work], 
									origin=SSAddressSSAddress_SSHome)
	SSAddress.getDnodes().append(SSAddressD1)
	SSAddressD2=probChoice(parent=SSAddress, name="SSAddressD2", 
									probs=["P_SSAddressSSAddress_workSSAddressD2"], 
									branches=[SSAddressSSAddress_work], 
									origin=SSAddressSSAddress_SSCtlg)
	SSAddress.getDnodes().append(SSAddressD2)
	SSAddressD3=probChoice(parent=SSAddress, name="SSAddressD3", 
									probs=["P_SSAddressSSAddress_workSSAddressD3"], 
									branches=[SSAddressSSAddress_work], 
									origin=SSAddressSSAddress_SSCarts)
	SSAddress.getDnodes().append(SSAddressD3)
	SSAddressD4=awsActivity(parent=SSAddress, name="SSAddressD4",activity=SSAddressSSAddress_work)
	SSAddress.getDnodes().append(SSAddressD4)
	
	
	###### SSHome logic
	
	###### SSHome activities and calls
	SSHomeSSHome_a1=Activity(stime=1.0E-4, parent=SSHome, name="SSHome_a1")
	SSHome.getActivities().append(SSHomeSSHome_a1)
	SSHomeSSHome_work=Activity(stime=1.0, parent=SSHome, name="SSHome_work")
	SSHome.getActivities().append(SSHomeSSHome_work)

	###### SSHome Activity Diagram
	# connect the entry to the main activity of function 
	SSHomeDI=probChoice(parent=SSHome, name="SSHomeDI", 
									probs=["P_SSHomeSSHome_a1"], 
									branches=[SSHomeSSHome_a1], 
									origin=SSHome)
	SSHome.getDnodes().append(SSHomeDI)
	SSHomeD0=probChoice(parent=SSHome, name="SSHomeD0", 
									probs=["P_SSHomeSSHome_workSSHomeD0"], 
									branches=[SSHomeSSHome_work], 
									origin=SSHomeSSHome_a1)
	SSHome.getDnodes().append(SSHomeD0)
	SSHomeD1=awsActivity(parent=SSHome, name="SSHomeD1",activity=SSHomeSSHome_work)
	SSHome.getDnodes().append(SSHomeD1)
	
	
	###### SSCtlg logic
	
	###### SSCtlg activities and calls
	SSCtlgSSCtlg_a1=Activity(stime=1.0E-4, parent=SSCtlg, name="SSCtlg_a1")
	SSCtlg.getActivities().append(SSCtlgSSCtlg_a1)
	SSCtlgSSCtlg_work=Activity(stime=1.0, parent=SSCtlg, name="SSCtlg_work")
	SSCtlg.getActivities().append(SSCtlgSSCtlg_work)
	SSCtlgSSCtlg_SSList=SynchCall(dest=SSList, parent=SSCtlg, name="SSCtlg_SSListToSSList")
	SSCtlg.getActivities().append(SSCtlgSSCtlg_SSList)
	SSCtlgSSCtlg_SSItem=SynchCall(dest=SSItem, parent=SSCtlg, name="SSCtlg_SSItemToSSItem")
	SSCtlg.getActivities().append(SSCtlgSSCtlg_SSItem)

	###### SSCtlg Activity Diagram
	# connect the entry to the main activity of function 
	SSCtlgDI=probChoice(parent=SSCtlg, name="SSCtlgDI", 
									probs=["P_SSCtlgSSCtlg_a1"], 
									branches=[SSCtlgSSCtlg_a1], 
									origin=SSCtlg)
	SSCtlg.getDnodes().append(SSCtlgDI)
	SSCtlgD0=probChoice(parent=SSCtlg, name="SSCtlgD0", 
									probs=["P_SSCtlgSSCtlg_SSListSSCtlgD0","P_SSCtlgSSCtlg_SSItemSSCtlgD0"], 
									branches=[SSCtlgSSCtlg_SSList,SSCtlgSSCtlg_SSItem], 
									origin=SSCtlgSSCtlg_a1)
	SSCtlg.getDnodes().append(SSCtlgD0)
	SSCtlgD1=probChoice(parent=SSCtlg, name="SSCtlgD1", 
									probs=["P_SSCtlgSSCtlg_workSSCtlgD1"], 
									branches=[SSCtlgSSCtlg_work], 
									origin=SSCtlgSSCtlg_SSList)
	SSCtlg.getDnodes().append(SSCtlgD1)
	SSCtlgD2=probChoice(parent=SSCtlg, name="SSCtlgD2", 
									probs=["P_SSCtlgSSCtlg_workSSCtlgD2"], 
									branches=[SSCtlgSSCtlg_work], 
									origin=SSCtlgSSCtlg_SSItem)
	SSCtlg.getDnodes().append(SSCtlgD2)
	SSCtlgD3=awsActivity(parent=SSCtlg, name="SSCtlgD3",activity=SSCtlgSSCtlg_work)
	SSCtlg.getDnodes().append(SSCtlgD3)
	
	
	###### SSCart logic
	
	###### SSCart activities and calls
	SSCartSSCart_a1=Activity(stime=1.0E-4, parent=SSCart, name="SSCart_a1")
	SSCart.getActivities().append(SSCartSSCart_a1)
	SSCartSSCart_work=Activity(stime=1.0, parent=SSCart, name="SSCart_work")
	SSCart.getActivities().append(SSCartSSCart_work)
	SSCartSSCart_SSGet=SynchCall(dest=SSGet, parent=SSCart, name="SSCart_SSGetToSSGet")
	SSCart.getActivities().append(SSCartSSCart_SSGet)
	SSCartSSCart_SSAdd=SynchCall(dest=SSAdd, parent=SSCart, name="SSCart_SSAddToSSAdd")
	SSCart.getActivities().append(SSCartSSCart_SSAdd)
	SSCartSSCart_SSDel=SynchCall(dest=SSDel, parent=SSCart, name="SSCart_SSDelToSSDel")
	SSCart.getActivities().append(SSCartSSCart_SSDel)

	###### SSCart Activity Diagram
	# connect the entry to the main activity of function 
	SSCartDI=probChoice(parent=SSCart, name="SSCartDI", 
									probs=["P_SSCartSSCart_a1"], 
									branches=[SSCartSSCart_a1], 
									origin=SSCart)
	SSCart.getDnodes().append(SSCartDI)
	SSCartD0=probChoice(parent=SSCart, name="SSCartD0", 
									probs=["P_SSCartSSCart_SSGetSSCartD0","P_SSCartSSCart_SSAddSSCartD0","P_SSCartSSCart_SSDelSSCartD0"], 
									branches=[SSCartSSCart_SSGet,SSCartSSCart_SSAdd,SSCartSSCart_SSDel], 
									origin=SSCartSSCart_a1)
	SSCart.getDnodes().append(SSCartD0)
	SSCartD1=probChoice(parent=SSCart, name="SSCartD1", 
									probs=["P_SSCartSSCart_workSSCartD1"], 
									branches=[SSCartSSCart_work], 
									origin=SSCartSSCart_SSGet)
	SSCart.getDnodes().append(SSCartD1)
	SSCartD2=probChoice(parent=SSCart, name="SSCartD2", 
									probs=["P_SSCartSSCart_workSSCartD2"], 
									branches=[SSCartSSCart_work], 
									origin=SSCartSSCart_SSAdd)
	SSCart.getDnodes().append(SSCartD2)
	SSCartD3=probChoice(parent=SSCart, name="SSCartD3", 
									probs=["P_SSCartSSCart_workSSCartD3"], 
									branches=[SSCartSSCart_work], 
									origin=SSCartSSCart_SSDel)
	SSCart.getDnodes().append(SSCartD3)
	SSCartD4=awsActivity(parent=SSCart, name="SSCartD4",activity=SSCartSSCart_work)
	SSCart.getDnodes().append(SSCartD4)
	
	
	###### SSList logic
	
	###### SSList activities and calls
	SSListSSList_a1=Activity(stime=1.0E-4, parent=SSList, name="SSList_a1")
	SSList.getActivities().append(SSListSSList_a1)
	SSListSSList_work=Activity(stime=1.0, parent=SSList, name="SSList_work")
	SSList.getActivities().append(SSListSSList_work)
	SSListSSList_Query=SynchCall(dest=SSCatQuery, parent=SSList, name="SSList_QueryToSSCatQuery")
	SSList.getActivities().append(SSListSSList_Query)

	###### SSList Activity Diagram
	# connect the entry to the main activity of function 
	SSListDI=probChoice(parent=SSList, name="SSListDI", 
									probs=["P_SSListSSList_a1"], 
									branches=[SSListSSList_a1], 
									origin=SSList)
	SSList.getDnodes().append(SSListDI)
	SSListD0=probChoice(parent=SSList, name="SSListD0", 
									probs=["P_SSListSSList_QuerySSListD0"], 
									branches=[SSListSSList_Query], 
									origin=SSListSSList_a1)
	SSList.getDnodes().append(SSListD0)
	SSListD1=probChoice(parent=SSList, name="SSListD1", 
									probs=["P_SSListSSList_workSSListD1"], 
									branches=[SSListSSList_work], 
									origin=SSListSSList_Query)
	SSList.getDnodes().append(SSListD1)
	SSListD2=awsActivity(parent=SSList, name="SSListD2",activity=SSListSSList_work)
	SSList.getDnodes().append(SSListD2)
	
	
	###### SSItem logic
	
	###### SSItem activities and calls
	SSItemSSItem_a1=Activity(stime=1.0E-4, parent=SSItem, name="SSItem_a1")
	SSItem.getActivities().append(SSItemSSItem_a1)
	SSItemSSItem_work=Activity(stime=1.0, parent=SSItem, name="SSItem_work")
	SSItem.getActivities().append(SSItemSSItem_work)
	SSItemSSItem_Query=SynchCall(dest=SSCatQuery, parent=SSItem, name="SSItem_QueryToSSCatQuery")
	SSItem.getActivities().append(SSItemSSItem_Query)

	###### SSItem Activity Diagram
	# connect the entry to the main activity of function 
	SSItemDI=probChoice(parent=SSItem, name="SSItemDI", 
									probs=["P_SSItemSSItem_a1"], 
									branches=[SSItemSSItem_a1], 
									origin=SSItem)
	SSItem.getDnodes().append(SSItemDI)
	SSItemD0=probChoice(parent=SSItem, name="SSItemD0", 
									probs=["P_SSItemSSItem_QuerySSItemD0"], 
									branches=[SSItemSSItem_Query], 
									origin=SSItemSSItem_a1)
	SSItem.getDnodes().append(SSItemD0)
	SSItemD1=probChoice(parent=SSItem, name="SSItemD1", 
									probs=["P_SSItemSSItem_workSSItemD1"], 
									branches=[SSItemSSItem_work], 
									origin=SSItemSSItem_Query)
	SSItem.getDnodes().append(SSItemD1)
	SSItemD2=awsActivity(parent=SSItem, name="SSItemD2",activity=SSItemSSItem_work)
	SSItem.getDnodes().append(SSItemD2)
	
	
	###### SSGet logic
	
	###### SSGet activities and calls
	SSGetSSGet_a1=Activity(stime=1.0E-4, parent=SSGet, name="SSGet_a1")
	SSGet.getActivities().append(SSGetSSGet_a1)
	SSGetSSGet_work=Activity(stime=1.0, parent=SSGet, name="SSGet_work")
	SSGet.getActivities().append(SSGetSSGet_work)
	SSGetSSGet_Query=SynchCall(dest=SSCartQuery, parent=SSGet, name="SSGet_QueryToSSCartQuery")
	SSGet.getActivities().append(SSGetSSGet_Query)

	###### SSGet Activity Diagram
	# connect the entry to the main activity of function 
	SSGetDI=probChoice(parent=SSGet, name="SSGetDI", 
									probs=["P_SSGetSSGet_a1"], 
									branches=[SSGetSSGet_a1], 
									origin=SSGet)
	SSGet.getDnodes().append(SSGetDI)
	SSGetD0=probChoice(parent=SSGet, name="SSGetD0", 
									probs=["P_SSGetSSGet_QuerySSGetD0"], 
									branches=[SSGetSSGet_Query], 
									origin=SSGetSSGet_a1)
	SSGet.getDnodes().append(SSGetD0)
	SSGetD1=probChoice(parent=SSGet, name="SSGetD1", 
									probs=["P_SSGetSSGet_workSSGetD1"], 
									branches=[SSGetSSGet_work], 
									origin=SSGetSSGet_Query)
	SSGet.getDnodes().append(SSGetD1)
	SSGetD2=awsActivity(parent=SSGet, name="SSGetD2",activity=SSGetSSGet_work)
	SSGet.getDnodes().append(SSGetD2)
	
	
	###### SSAdd logic
	
	###### SSAdd activities and calls
	SSAddSSAdd_a1=Activity(stime=1.0E-4, parent=SSAdd, name="SSAdd_a1")
	SSAdd.getActivities().append(SSAddSSAdd_a1)
	SSAddSSAdd_work=Activity(stime=1.0, parent=SSAdd, name="SSAdd_work")
	SSAdd.getActivities().append(SSAddSSAdd_work)
	SSAddSSAdd_Query=SynchCall(dest=SSCartQuery, parent=SSAdd, name="SSAdd_QueryToSSCartQuery")
	SSAdd.getActivities().append(SSAddSSAdd_Query)

	###### SSAdd Activity Diagram
	# connect the entry to the main activity of function 
	SSAddDI=probChoice(parent=SSAdd, name="SSAddDI", 
									probs=["P_SSAddSSAdd_a1"], 
									branches=[SSAddSSAdd_a1], 
									origin=SSAdd)
	SSAdd.getDnodes().append(SSAddDI)
	SSAddD0=probChoice(parent=SSAdd, name="SSAddD0", 
									probs=["P_SSAddSSAdd_QuerySSAddD0"], 
									branches=[SSAddSSAdd_Query], 
									origin=SSAddSSAdd_a1)
	SSAdd.getDnodes().append(SSAddD0)
	SSAddD1=probChoice(parent=SSAdd, name="SSAddD1", 
									probs=["P_SSAddSSAdd_workSSAddD1"], 
									branches=[SSAddSSAdd_work], 
									origin=SSAddSSAdd_Query)
	SSAdd.getDnodes().append(SSAddD1)
	SSAddD2=awsActivity(parent=SSAdd, name="SSAddD2",activity=SSAddSSAdd_work)
	SSAdd.getDnodes().append(SSAddD2)
	
	
	###### SSDel logic
	
	###### SSDel activities and calls
	SSDelSSDel_a1=Activity(stime=1.0E-4, parent=SSDel, name="SSDel_a1")
	SSDel.getActivities().append(SSDelSSDel_a1)
	SSDelSSDel_work=Activity(stime=1.0, parent=SSDel, name="SSDel_work")
	SSDel.getActivities().append(SSDelSSDel_work)
	SSDelSSDel_Query=SynchCall(dest=SSCartQuery, parent=SSDel, name="SSDel_QueryToSSCartQuery")
	SSDel.getActivities().append(SSDelSSDel_Query)

	###### SSDel Activity Diagram
	# connect the entry to the main activity of function 
	SSDelDI=probChoice(parent=SSDel, name="SSDelDI", 
									probs=["P_SSDelSSDel_a1"], 
									branches=[SSDelSSDel_a1], 
									origin=SSDel)
	SSDel.getDnodes().append(SSDelDI)
	SSDelD0=probChoice(parent=SSDel, name="SSDelD0", 
									probs=["P_SSDelSSDel_QuerySSDelD0"], 
									branches=[SSDelSSDel_Query], 
									origin=SSDelSSDel_a1)
	SSDel.getDnodes().append(SSDelD0)
	SSDelD1=probChoice(parent=SSDel, name="SSDelD1", 
									probs=["P_SSDelSSDel_workSSDelD1"], 
									branches=[SSDelSSDel_work], 
									origin=SSDelSSDel_Query)
	SSDel.getDnodes().append(SSDelD1)
	SSDelD2=awsActivity(parent=SSDel, name="SSDelD2",activity=SSDelSSDel_work)
	SSDel.getDnodes().append(SSDelD2)
	
	
	###### SSCatQuery logic
	
	###### SSCatQuery activities and calls
	SSCatQuerySSCatQuery_a1=Activity(stime=1.0E-4, parent=SSCatQuery, name="SSCatQuery_a1")
	SSCatQuery.getActivities().append(SSCatQuerySSCatQuery_a1)
	SSCatQuerySSCatQuery_work=Activity(stime=1.0, parent=SSCatQuery, name="SSCatQuery_work")
	SSCatQuery.getActivities().append(SSCatQuerySSCatQuery_work)

	###### SSCatQuery Activity Diagram
	# connect the entry to the main activity of function 
	SSCatQueryDI=probChoice(parent=SSCatQuery, name="SSCatQueryDI", 
									probs=["P_SSCatQuerySSCatQuery_a1"], 
									branches=[SSCatQuerySSCatQuery_a1], 
									origin=SSCatQuery)
	SSCatQuery.getDnodes().append(SSCatQueryDI)
	SSCatQueryD0=probChoice(parent=SSCatQuery, name="SSCatQueryD0", 
									probs=["P_SSCatQuerySSCatQuery_workSSCatQueryD0"], 
									branches=[SSCatQuerySSCatQuery_work], 
									origin=SSCatQuerySSCatQuery_a1)
	SSCatQuery.getDnodes().append(SSCatQueryD0)
	SSCatQueryD1=awsActivity(parent=SSCatQuery, name="SSCatQueryD1",activity=SSCatQuerySSCatQuery_work)
	SSCatQuery.getDnodes().append(SSCatQueryD1)
	
	
	###### SSCartQuery logic
	
	###### SSCartQuery activities and calls
	SSCartQuerySSCartQuery_a1=Activity(stime=1.0E-4, parent=SSCartQuery, name="SSCartQuery_a1")
	SSCartQuery.getActivities().append(SSCartQuerySSCartQuery_a1)
	SSCartQuerySSCartQuery_work=Activity(stime=1.0, parent=SSCartQuery, name="SSCartQuery_work")
	SSCartQuery.getActivities().append(SSCartQuerySSCartQuery_work)

	###### SSCartQuery Activity Diagram
	# connect the entry to the main activity of function 
	SSCartQueryDI=probChoice(parent=SSCartQuery, name="SSCartQueryDI", 
									probs=["P_SSCartQuerySSCartQuery_a1"], 
									branches=[SSCartQuerySSCartQuery_a1], 
									origin=SSCartQuery)
	SSCartQuery.getDnodes().append(SSCartQueryDI)
	SSCartQueryD0=probChoice(parent=SSCartQuery, name="SSCartQueryD0", 
									probs=["P_SSCartQuerySSCartQuery_workSSCartQueryD0"], 
									branches=[SSCartQuerySSCartQuery_work], 
									origin=SSCartQuerySSCartQuery_a1)
	SSCartQuery.getDnodes().append(SSCartQueryD0)
	SSCartQueryD1=awsActivity(parent=SSCartQuery, name="SSCartQueryD1",activity=SSCartQuerySSCartQuery_work)
	SSCartQuery.getDnodes().append(SSCartQueryD1)
	
	LQN={"tasks":[T_SockClient ,T_SSAddress,T_SSHome,T_SSCtlg,T_SSCart,T_SSList,T_SSItem,T_SSGet,T_SSAdd,T_SSDel,T_SSCatQuery,T_SSCartQuery], "name":"sockshop"}
	lqn2mpp.getMPP(lqn=LQN)
	#lqn2mpp.removeInfSynch()
	#lqn2mpp.removeInfAsynch()
	#lqn2mpp.removeInfAcquire()
	lqn2mpp.toMatlab(outDir="./")
	#lqn2mpp.toLqns(outDir="model",LQN=LQN)
	