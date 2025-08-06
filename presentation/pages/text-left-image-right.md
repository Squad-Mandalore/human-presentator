# Umgang mit Misserfolg
<div>
<p><strong>"Your current level of knowledge is insufficient to be successful in an intern position"</strong></p>
</div>
<div class="grid grid-cols-[50%_50%] gap-4" style="height: 60%">
  <!-- First column -->
  <div class="vertical-center">
    <ul style="padding-left: 20px;">
      <div v-click="1">
      <li>Linux
        <ul class="dash-list">
          <li>"Start to use it as your main OS"</li>
        </ul>
      </li>
      </div>
      <div v-click="2">
      <li>Docker
        <ul class="dash-list">
          <li>
            "Get more familiar with containers theory"
          </li>
        </ul>
      </li>
      </div>
      <div v-click="3">
      <li>Networking
        <ul class="dash-list">
          <li>"Use your linux box as a router"</li>
        </ul>
      </li>
      </div>
      <div v-click="4">
      <li>Kubernetes
        <ul class="dash-list">
          <li>"Learn basic Kubernetes concepts"</li>
        </ul>
      </li>
      </div>
      <div v-click="5">
      <li>CI/CD
        <ul class="dash-list">
          <li>"Try to write a CI/CD pipeline"</li>
        </ul>
      </li>
      </div>
    </ul>
  </div>
  <!-- Second column -->
  <div class="vertical-center-img">
    <img src="/dev-ops.png" alt="heh" width="100%" height="100%" class="center">
  </div>
</div>

<Footer />

<style>
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
p {
  margin-top: 1rem;
  margin-bottom: 0rem;
}
.vertical-center {
  display: block;
  justify-content: center;
  align-items: center;
  height: 100%;
}
.vertical-center-img {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}
ul.dash-list li::before {
  content: "- ";
}
ul.dash-list {
  list-style-type: none;
}
</style>
