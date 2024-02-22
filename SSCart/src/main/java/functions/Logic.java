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
	private static final Logger logger = Logger.getLogger("SSCart");
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
	public void SSCart_a1(){
		this.act_exec.put("SSCart_a1", true);
		this.doWork(1.0E-4);
	}
	public void SSCart_work(){
		this.act_exec.put("SSCart_work", true);
		this.doWork(1.0);
	}
	public void SSCart_SSGet(){
		this.act_exec.put("SSCart_SSGet", true);
		this.doWork(1.0E-4);
		String url = "https://northamerica-northeast1-modellearning.cloudfunctions.net/ssget";
		var getRequest = java.net.http.HttpRequest.newBuilder().uri(URI.create(url)).GET().build();

		try {
			var getResponse = Logic.client.send(getRequest, BodyHandlers.ofString());
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	public void SSCart_SSAdd(){
		this.act_exec.put("SSCart_SSAdd", true);
		this.doWork(1.0E-4);
		String url = "https://northamerica-northeast1-modellearning.cloudfunctions.net/ssadd";
		var getRequest = java.net.http.HttpRequest.newBuilder().uri(URI.create(url)).GET().build();

		try {
			var getResponse = Logic.client.send(getRequest, BodyHandlers.ofString());
		} catch (IOException e) {
			e.printStackTrace();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
	public void SSCart_SSDel(){
		this.act_exec.put("SSCart_SSDel", true);
		this.doWork(1.0E-4);
		String url = "https://northamerica-northeast1-modellearning.cloudfunctions.net/ssdel";
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
	public void OrNode_SSCart_a1(){
		//OrNode Logic
		List<Pair<String, Double>> distributionData = new ArrayList<>();
		distributionData.add(new Pair<>("SSCart_SSGet", 0.3333));
		distributionData.add(new Pair<>("SSCart_SSAdd", 0.3333));
		distributionData.add(new Pair<>("SSCart_SSDel", 0.3333));
		EnumeratedDistribution<String> distribution = new EnumeratedDistribution<>(distributionData);
		String randomChoice = distribution.sample();
		if(randomChoice=="SSCart_SSGet"){
			SSCart_SSGet();
		}
		if(randomChoice=="SSCart_SSAdd"){
			SSCart_SSAdd();
		}
		if(randomChoice=="SSCart_SSDel"){
			SSCart_SSDel();
		}
	}
	public void OrNode_SSCart_SSGet(){
		//OrNode Logic
		List<Pair<String, Double>> distributionData = new ArrayList<>();
		distributionData.add(new Pair<>("SSCart_work", 1.0));
		EnumeratedDistribution<String> distribution = new EnumeratedDistribution<>(distributionData);
		String randomChoice = distribution.sample();
		if(randomChoice=="SSCart_work"){
			SSCart_work();
		}
	}
	public void OrNode_SSCart_SSAdd(){
		//OrNode Logic
		List<Pair<String, Double>> distributionData = new ArrayList<>();
		distributionData.add(new Pair<>("SSCart_work", 1.0));
		EnumeratedDistribution<String> distribution = new EnumeratedDistribution<>(distributionData);
		String randomChoice = distribution.sample();
		if(randomChoice=="SSCart_work"){
			SSCart_work();
		}
	}
	public void OrNode_SSCart_SSDel(){
		//OrNode Logic
		List<Pair<String, Double>> distributionData = new ArrayList<>();
		distributionData.add(new Pair<>("SSCart_work", 1.0));
		EnumeratedDistribution<String> distribution = new EnumeratedDistribution<>(distributionData);
		String randomChoice = distribution.sample();
		if(randomChoice=="SSCart_work"){
			SSCart_work();
		}
	}
	public void ReplyNode_SSCart_work(){
		//ReplyNode Logic
		BufferedWriter writer;
		try {
			writer = this.response.getWriter();
			writer.write("SSCart_work[SSCart]");
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
		SSCart_a1();
		//execetute the decision node of already executed evt
		if(this.act_exec.get("SSCart_a1")!=null && this.act_exec.get("SSCart_a1")) {
		  this.act_exec.put("SSCart_a1",false);
		  OrNode_SSCart_a1();
		}
		if(this.act_exec.get("SSCart_SSGet")!=null && this.act_exec.get("SSCart_SSGet")) {
		  this.act_exec.put("SSCart_SSGet",false);
		  OrNode_SSCart_SSGet();
		}
		if(this.act_exec.get("SSCart_SSAdd")!=null && this.act_exec.get("SSCart_SSAdd")) {
		  this.act_exec.put("SSCart_SSAdd",false);
		  OrNode_SSCart_SSAdd();
		}
		if(this.act_exec.get("SSCart_SSDel")!=null && this.act_exec.get("SSCart_SSDel")) {
		  this.act_exec.put("SSCart_SSDel",false);
		  OrNode_SSCart_SSDel();
		}
		if(this.act_exec.get("SSCart_work")!=null && this.act_exec.get("SSCart_work")) {
		  this.act_exec.put("SSCart_work",false);
		  ReplyNode_SSCart_work();
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
