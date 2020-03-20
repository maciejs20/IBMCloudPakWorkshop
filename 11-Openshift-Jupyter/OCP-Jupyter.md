# IBM Cloud Container Workshop

###### *Version: 2020-03-03*

---

# OpenShift S2I based on Docker Image: Jupiter

---

![image-20181018184328603](/Users/maciej/Documents/00_IBM/Produkty/ICP/00_Workshops/Container WS Lectures/Labs-git/8-Openshift/1-OpenShift-Lab.assets/image-20181018184328603.png)





##  Introduction

During this lab we will be using S2I mechanism together with Docker image

![image-20200318093216158](OCP-Jupyter.assets/image-20200318093216158.png)

Be sure that you have your **labuser**xx userID with xx representing a number from 00 to 99. You also have been set a password associated to labuserxx. 

Don't use someone else userID except if the instructor ask you to do so. 



**This lab is based on Openshift 4.2.** 



We will be using ready made Dockerfile for R-Notebook, available at

https://github.com/jupyter/docker-stacks/tree/master/r-notebook





## 3 - OpenShift Web Console

Get back to Your VNC client and go to the OpenShift Web Console (use your credentials if necessary)

https://console-openshift-console.apps.a.cloudpak.site/dashboards

If asked, pick "htpasswd" as "Log in with...".

Login using credentials provided (labprojxx)



On the right side, click on the blue link : **labproj<xx>**

![image-20191012141253852](images/image-20191012141253852-0882373.png)



You will switch from the `Service Catalog` to the `Application Console` 

![image-20191012140139136](images/image-20191012140139136-0881699.png)

to the `Application Console` 

![image-20191012140049135](images/image-20191012140049135-0881649.png)

This will show the new created application:

![1-OpenShift-Lab.assets/image-20200107095718881.png](1-OpenShift-Lab.assets/image-20200107095718881.png)

> The name of your application, the number of pod, the application URL link ...



Click on the `nodejs-ex, #1` blue link, then you will see some more details on the application: 

![image-20191012140537676](images/image-20191012140537676-0881937.png)



Walk thru all the buttons : 

![image-20191012141505750](images/image-20191012141505750-0882505.png)

## 

On the left side, click on **Pods**:

![image-20191012140923841](images/image-20191012140923841-0882163.png)



Click on the **running** Pod:

![image-20191012141622463](images/image-20191012141622463-0882582.png)

You will get this page:

![1-OpenShift-Lab.assets/image-20200107095905478.png](1-OpenShift-Lab.assets/image-20200107095905478.png)

Walk thru the different links to understand this application:

![image-20191012141800412](images/image-20191012141800412-0882680.png)

Like for example the logs:

![image-20191012141837264](images/image-20191012141837264-0882717.png)



Now, on the left part of the screen, click on `deployments`

![image-20191012142416925](images/image-20191012142416925-0883056.png)



Then click on the blue link `nodes-ex`

![image-20191012142541243](images/image-20191012142541243-0883141.png)

Click on the Actions button:

![image-20191012142706939](images/image-20191012142706939-0883227.png)

Then click on `Edit YAML`to look at the kubernetes resource definition:

![image-20191012142755397](images/image-20191012142755397-0883275.png)

 You will recognize the definition deploymentconfig, similar to Kubernetes deployment. 

Finally from the left side of the screen, click on `routes`

![image-20191012143052666](images/image-20191012143052666-0883452.png)

And you will see the route definition for that deployment: 

![image-20191012143150770](images/image-20191012143150770-0883510.png)

Open Your route (**nodejs-ex**), than click on "**Actions**" -> "**Edit Yaml**" to see the route definition

![image-20191012143231692](images/image-20191012143231692-0883551.png)

 Click "**Cancel**"

## 4 - Monitoring your application

To learn about monitoring of your application, on the left pane, click on the `Monitoring`icon:

![image-20191012145519383](images/image-20191012145519383-0884919.png)

You should see all the resources involved into your application in the cluster:

![image-20191012145611519](images/image-20191012145611519-0884971.png)

Walk thru some itmes like Pods or Builds where you can see some of the previous pages in this lab.

Go to Deployments (nodes-ex) and open the #1

![image-20191012145944647](images/image-20191012145944647-0885184.png)

Finally, increase the number of pods (**not too much** - 2). There is a limit set on the number of pods running in our system.

![image-20191012150046190](images/image-20191012150046190-0885246.png)

And after a while, you will see 2 active pods:

![image-20191012150140360](images/image-20191012150140360-0885300.png)

And at the bottom of the page:

![image-20191012150231361](images/image-20191012150231361-0885351.png)

This mens that now 2 pods are serving the requests. 

Now click on one of these new pods and you should a page like this one:

![image-20191012152905816](images/image-20191012152905816-0886945.png) 

Let's try a crazy experience and kill this pod ! click on the action button and select `delete`

![image-20191012153102475](images/image-20191012153102475-0887062.png)

The following popup window will appear:

![image-20191012153151649](images/image-20191012153151649-0887111.png)

Click on `Delete` and you should see breifly your pod terminating.

![image-20191012153249281](images/image-20191012153249281-0887169.png)



A new pod is automatically started !!! Because the number of replicaset has been defined to **2** , even if a pod is crashing, it will be replace automatically by a new one. 

![image-20191012153424224](images/image-20191012153424224-0887264.png)

## 5 - Clean the application

Clean the system - delete the application created.

The system has created a few comonents. As our resources are limited, before we will start fith further labs we need to delete the application created.

### 1. Clean the deployment

Select "**Applications**" -> "**Deployments**" from the web console menu on the left.

Click on the application that You have created:

![1-OpenShift-Lab.assets/image-20200107100359449.png](1-OpenShift-Lab.assets/image-20200107100359449.png)



From the **"Actions"** select "**Delete**". Confirm with "**Delete**" again.

## 



## Conclusion

You successfully installed and used the oc CLI and the OpenShift web console thru the installation of a typical Node.JS application (from Github). 

You noticed the following details:

- easy to access the OpenShift web console
- easy to build and deploy the application, the container, the pod.
- easy to scale up and down 
- automatic healing

You also noticed the difference between Kubernetes and OpenShift like 

- the route concept
- the wildcard DNS utilization
- the image stream and S2I concepts to build the docker image

**Congrats**

----

----



# End of Lab



