# Cloud Pak for Application Lab - short version





# Part 2: OpenShift



![image-20191012152122962](OpenshiftLab.assets/image-20191012152122962-0886483.png)





##  Introduction

During this lab, we are going to set up your laptop to be prepared to all labs during this workshop. You should be able to connect to an **OpenShift** Cluster thru the Web Console and navigate thru the different kubernetes resources.



![image-20191116105934442](OpenshiftLab.assets/image-20191116105934442-3898374.png)


As you can see on the picture, you will connect to the OpenShift Cluster Web UI to the Master for management and development purposes. The end-users will connect to the applications thru the Infra Node.



The instructor will give you:

- a user ID and password to connect to the cluster. The user ID is in the format **labuser<xx>** where xx is a number from 00 to 99. Don't use someone else userID except if the instructor ask you to do so. 
- a project name in the format **labproj<xx>**. Each project is associated to the corresponding labuser<xx>. 



## 2.1 Create simple deployment in the OpenShift Web GUI

### Connect to the server

We have desktop service provisioned on the lab server, accesible via VNC. 

If You don't have vnc client, get it from https://www.realvnc.com/en/connect/download/viewer/ or any other source.

Use the vnc client and connect to the lab27 server. Please double check the port number that this service runs!

![image-20200303103548919](/Users/maciej/Documents/00_IBM/Produkty/ICP/00_Workshops/Container WS Lectures/Labs-git/101-ShortCPLab/OpenshiftLab.assets/image-20200303103548919.png)



### Connect to the Web Console

Select Applications->Internet and open firefox browser

![image-20200303103637780](/Users/maciej/Documents/00_IBM/Produkty/ICP/00_Workshops/Container WS Lectures/Labs-git/101-ShortCPLab/OpenshiftLab.assets/image-20200303103637780.png)

You can now use the following URL :

```http
https://master.x.cloudpak.site:8443
```

Please take a note of this link because we will use it very often. 

**This server is accesible ONLY via the VNC session, so do not try to open it from Your local web browser!**



Our server is using self-signed certificate, which may be identified by the browser as security risk.

Accept any security risk You may encounter (Advanced->Accept Risk and continue).



You are presented with Openshift login page.

![image-20191008154755641](/Users/maciej/Documents/00_IBM/Produkty/ICP/00_Workshops/Container WS Lectures/Labs-git/101-ShortCPLab/OpenshiftLab.assets/image-20191008154755641-0542475.png)



Type your credentials (**user ID, password**) and click **Log in**

![image-20191008154849227](/Users/maciej/Documents/00_IBM/Produkty/ICP/00_Workshops/Container WS Lectures/Labs-git/101-ShortCPLab/OpenshiftLab.assets/image-20191008154849227-0542529.png)



### Deploy the app 

We have created the image during the kubernetes lab. Let's reuse that and deploy application using Openshift Web GUI to see how simple it is



From the **catalog console**, pick "Deploy Image"

![image-20200320144257328](OpenshiftLab.assets/image-20200320144257328.png)



Now set the fields:

- Add to Porject: pick Your project, as given by IBM Staff
- For Image Stream Tag: Namespace: pick Your project, as given by IBM Staff
- For Image Stream Tag: Image Stream: pick the image that we have created (hello1)
- For Image Stream Tag: Tag: pick the "2" tag
- For Name: leave "hello1"



|                                                              |
| :----------------------------------------------------------- |
| ![image-20200320144936288](OpenshiftLab.assets/image-20200320144936288.png) |



Click on "Deploy" and later on "Continue to project overview"

<table><tr><td>
<img src="OpenshiftLab.assets/image-20200320145040701.png" alt="image-20200320145040701" style="zoom:100%;" />
</td></tr></table>



### Expose the app

Expand the hello1 deployment with ">" icon:

![image-20200320145733603](OpenshiftLab.assets/image-20200320145733603.png)



Expose the app - click on "Routes-External Traffic: Create Route"

![image-20200320145853300](OpenshiftLab.assets/image-20200320145853300.png)



Do not change anything, just click on "**Create**"



### Check if app works

After a while You will be presented with the url created especially for Your deployment. Click on that in order to connect to the application.

![image-20200320150118986](OpenshiftLab.assets/image-20200320150118986.png)



### Scale the app

Increase the number of pods by using scaller steering controls on the deployment page.

Remember about the resource limits that are set on the cluster!

![image-20200320150527342](OpenshiftLab.assets/image-20200320150527342.png)



### Check the logs and events

Click on the "three dot" icon on the deployment header and pick "View logs".

![image-20200320150750845](OpenshiftLab.assets/image-20200320150750845.png)



Read thru the Logs" and "Events" to verify the app output and state.

When finished go to the "Details" tab to see pods.

![image-20200320151046484](OpenshiftLab.assets/image-20200320151046484.png)



### Delete the deployment

Now let's learn how to access our deployment from the OpenShift menu and how to delete the deployment. Using the menu on the left click on "**Applications"** -> "**Deployments"**, than pick **"hello1"**

![image-20200320151520592](OpenshiftLab.assets/image-20200320151520592.png)



Click on **"Actions" ->> "Delete"** to clear the deployment, confirm with "Delete"

### Delete the Service and Route

Use the:

- **Applications -> Services -> hello1 -> Actions -> Delete** to delete the service created
- **Applications -> Routes -> hello1 -> Actions -> Delete** to delete the route created



---



## 2.2 Utilize the S2I in OpenShift Web GUI

In this lab we will get familiar with the Source-To-Image mechanism, that allows to deploy the application from Your code repository  easily.

![image-20200320152345364](OpenshiftLab.assets/image-20200320152345364.png)

In the previous exercise we have used pre-made container with all the runtime and apllication code. We were responsible for all the container configuration and build. 

Openshift offers different deployment options, including the Source-To-Image that gets application source code from the git repo and created the container automatically.

We will be using sample (and simple) code published here: https://github.com/maciejs20/IBMCloudPakWorkshop/tree/master/Code/1

Please note that there is no Dockerfile in this repo!

![image-20200320154913610](OpenshiftLab.assets/image-20200320154913610.png)

### Log in to the cluster and access the catalog

Go to Your VNC client, open web browser and navigate to our cluster at https://master.x.cloudpak.site:8443

Login using credentials provided by IBM  (Openshift Cluster Account)



You are presented with cluster catalog.

![image-20200320152634214](OpenshiftLab.assets/image-20200320152634214.png)

Navigate to **Languages** tab shown on “Browse Catalog” tab

### Create application from python code

Select **"Python"** category and click on **"Python"** icon to start runtime configuration. The system will present You with a creator.

Click **Next** on the first page of the creator.

In the **"Configuration"** select:

- **Add to project** - select Your project (labprojxx)
- **Version** -  3.6

click on **"advanced options"** in the bottom of the screen to open detailed configuration.

Fill remaining fields as follows:

- **Application name** as mypython
- **Git repository URL** as “https://github.com/maciejs20/IBMCloudPakWorkshop.git”
- **Context Dir** as "Code/1"

Leave all remaining fields at it's defaults. Scroll down and click on "**Create**"

![image-20200320154026026](OpenshiftLab.assets/image-20200320154026026.png)



Now go to the **"Builds -> Builds -> mypython** to see all builds for this app. There is only one item available: #1 - the first build. Click on #1 to open the details.

Now verify "Logs" and "Events" to check if the build was successful.



### Access the app created

Now go to the **"Applications -> Routes -> mypython** and click on the app url

![image-20200320154513724](OpenshiftLab.assets/image-20200320154513724.png)

"Hello World" message shows, that the application has been created properly.

---

Let's this concludes the lab