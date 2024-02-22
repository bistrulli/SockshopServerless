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
	private static final Logger logger = Logger.getLogger("SSDel");
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
	public void SSDel_a1(){
		this.act_exec.put("SSDel_a1", true);
		this.doWork(1.0E-4);
	}
	public void SSDel_work(){
		this.act_exec.put("SSDel_work", true);
		this.doWork(1.0);
	}
	public void SSDel_Query(){
		this.act_exec.put("SSDel_Query", true);
		this.doWork(1.0E-4);
		String url = "https://northamerica-northeast1-modellearning.cloudfunctions.net/SSCartQuery";
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
	public void OrNode_SSDel_a1(){
		//OrNode Logic
		List<Pair<String, Double>> distributionData = new ArrayList<>();
		distributionData.add(new Pair<>("SSDel_Query", 1.0));
		EnumeratedDistribution<String> distribution = new EnumeratedDistribution<>(distributionData);
		String randomChoice = distribution.sample();
		if(randomChoice=="SSDel_Query"){
			SSDel_Query();
		}
	}
	public void OrNode_SSDel_Query(){
		//OrNode Logic
		List<Pair<String, Double>> distributionData = new ArrayList<>();
		distributionData.add(new Pair<>("SSDel_work", 1.0));
		EnumeratedDistribution<String> distribution = new EnumeratedDistribution<>(distributionData);
		String randomChoice = distribution.sample();
		if(randomChoice=="SSDel_work"){
			SSDel_work();
		}
	}
	public void ReplyNode_SSDel_work(){
		//ReplyNode Logic
		BufferedWriter writer;
		try {
			writer = this.response.getWriter();
			writer.write("SSDel_work[SSDel]");
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
		SSDel_a1();
		//execetute the decision node of already executed evt
		if(this.act_exec.get("SSDel_a1")!=null && this.act_exec.get("SSDel_a1")) {
		  this.act_exec.put("SSDel_a1",false);
		  OrNode_SSDel_a1();
		}
		if(this.act_exec.get("SSDel_Query")!=null && this.act_exec.get("SSDel_Query")) {
		  this.act_exec.put("SSDel_Query",false);
		  OrNode_SSDel_Query();
		}
		if(this.act_exec.get("SSDel_work")!=null && this.act_exec.get("SSDel_work")) {
		  this.act_exec.put("SSDel_work",false);
		  ReplyNode_SSDel_work();
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
