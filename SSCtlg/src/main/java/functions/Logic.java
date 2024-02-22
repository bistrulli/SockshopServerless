package functions;

import java.io.BufferedWriter;
import java.io.IOException;
import java.lang.management.ManagementFactory;
import java.lang.management.ThreadMXBean;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpResponse.BodyHandlers;
import java.time.Duration;
import java.util.logging.Logger;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.lang.Thread;

import org.apache.commons.math3.distribution.ExponentialDistribution;
import org.apache.commons.math3.distribution.EnumeratedDistribution;
import org.apache.commons.math3.util.Pair;

import com.google.cloud.functions.HttpFunction;
import com.google.cloud.functions.HttpRequest;
import com.google.cloud.functions.HttpResponse;

public class Logic implements HttpFunction {
	private static final Logger logger = Logger.getLogger("SSCtlg");
	private static ThreadMXBean mgm = ManagementFactory.getThreadMXBean();
	private static HttpClient client = HttpClient.newBuilder().connectTimeout(Duration.ofSeconds(180)).build();
	private HttpResponse response = null;
	private HashMap<String, Boolean> act_exec=new HashMap<String, Boolean>();
	private HashMap<String, Thread> act_thread=new HashMap<String, Thread>();
	private Long  startCpuTime=null;
	private Long  startExecTime=null;
	

	/*
	 * activities
	 */
	public void SSCtlg_a1(){
		this.act_exec.put("SSCtlg_a1", true);
		this.doWork(1.0E-4);
	}
	public void SSCtlg_work(){
		this.act_exec.put("SSCtlg_work", true);
		this.doWork(1.0);
	}
	public void SSCtlg_SSList(){
		this.act_exec.put("SSCtlg_SSList", true);
		this.doWork(1.0E-4);
		String url = "https://northamerica-northeast1-modellearning.cloudfunctions.net/SSList";
		var getRequest = java.net.http.HttpRequest.newBuilder().uri(URI.create(url)).GET().build();

		try {
			var getResponse = Logic.client.send(getRequest, BodyHandlers.ofString());
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	public void SSCtlg_SSItem(){
		this.act_exec.put("SSCtlg_SSItem", true);
		this.doWork(1.0E-4);
		String url = "https://northamerica-northeast1-modellearning.cloudfunctions.net/SSItem";
		var getRequest = java.net.http.HttpRequest.newBuilder().uri(URI.create(url)).GET().build();

		try {
			var getResponse = Logic.client.send(getRequest, BodyHandlers.ofString());
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}

	/*
	 * Dnodes
	 */
	public void OrNode_SSCtlg_a1(){
		//OrNode Logic
		List<Pair<String, Double>> distributionData = new ArrayList<>();
		distributionData.add(new Pair<>("SSCtlg_SSList", 0.5));
		distributionData.add(new Pair<>("SSCtlg_SSItem", 0.5));
		EnumeratedDistribution<String> distribution = new EnumeratedDistribution<>(distributionData);
		String randomChoice = distribution.sample();
		if(randomChoice=="SSCtlg_SSList"){
			SSCtlg_SSList();
		}
		if(randomChoice=="SSCtlg_SSItem"){
			SSCtlg_SSItem();
		}
	}
	public void OrNode_SSCtlg_SSList(){
		//OrNode Logic
		List<Pair<String, Double>> distributionData = new ArrayList<>();
		distributionData.add(new Pair<>("SSCtlg_work", 1.0));
		EnumeratedDistribution<String> distribution = new EnumeratedDistribution<>(distributionData);
		String randomChoice = distribution.sample();
		if(randomChoice=="SSCtlg_work"){
			SSCtlg_work();
		}
	}
	public void OrNode_SSCtlg_SSItem(){
		//OrNode Logic
		List<Pair<String, Double>> distributionData = new ArrayList<>();
		distributionData.add(new Pair<>("SSCtlg_work", 1.0));
		EnumeratedDistribution<String> distribution = new EnumeratedDistribution<>(distributionData);
		String randomChoice = distribution.sample();
		if(randomChoice=="SSCtlg_work"){
			SSCtlg_work();
		}
	}
	public void ReplyNode_SSCtlg_work(){
		//ReplyNode Logic
		BufferedWriter writer;
		try {
			writer = this.response.getWriter();
			writer.write("SSCtlg_work[SSCtlg]");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	@Override
	public void service(HttpRequest request, HttpResponse response) throws IOException {
		this.response = response;
		mgm.setThreadCpuTimeEnabled(true);
		this.startCpuTime=mgm.getCurrentThreadCpuTime();
		this.startExecTime=System.nanoTime();
		
		//execute the entry activity
		SSCtlg_a1();
		//execetute the decision node of already executed evt
		if(this.act_exec.get("SSCtlg_a1")!=null && this.act_exec.get("SSCtlg_a1")) {
		  this.act_exec.put("SSCtlg_a1",false);
		  OrNode_SSCtlg_a1();
		}
		if(this.act_exec.get("SSCtlg_SSList")!=null && this.act_exec.get("SSCtlg_SSList")) {
		  this.act_exec.put("SSCtlg_SSList",false);
		  OrNode_SSCtlg_SSList();
		}
		if(this.act_exec.get("SSCtlg_SSItem")!=null && this.act_exec.get("SSCtlg_SSItem")) {
		  this.act_exec.put("SSCtlg_SSItem",false);
		  OrNode_SSCtlg_SSItem();
		}
		if(this.act_exec.get("SSCtlg_work")!=null && this.act_exec.get("SSCtlg_work")) {
		  this.act_exec.put("SSCtlg_work",false);
		  ReplyNode_SSCtlg_work();
		}
		String logstring=String.format("cpu:=%d  rt:=%d",mgm.getCurrentThreadCpuTime()-this.startCpuTime,
									   System.nanoTime()-this.startExecTime);
		Logic.logger.info(logstring);
	}

	private void doWork(Double stime) {
		ExponentialDistribution dist = new ExponentialDistribution(stime);
		long delay = Long.valueOf(Math.round(dist.sample() * 1e9));
		long start = mgm.getCurrentThreadCpuTime();
		while ((mgm.getCurrentThreadCpuTime() - start) < delay) {
		}
	}
}
