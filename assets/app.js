(function () {
  "use strict";

  // Reveal on scroll
  var reveals = Array.prototype.slice.call(document.querySelectorAll(".reveal"));
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  // Lightbox for the Gantt figures
  var lightbox = document.querySelector(".lightbox");
  var lightboxImg = lightbox ? lightbox.querySelector("img") : null;

  function openLightbox(src, alt) {
    if (!lightbox || !src) return;
    lightboxImg.src = src;
    lightboxImg.alt = alt || "Planning Gantt — enlarged";
    lightbox.hidden = false;
    document.body.style.overflow = "hidden";
  }

  function closeLightbox() {
    if (!lightbox || lightbox.hidden) return;
    lightbox.hidden = true;
    lightboxImg.removeAttribute("src");
    document.body.style.overflow = "";
  }

  Array.prototype.forEach.call(document.querySelectorAll(".zoom"), function (btn) {
    btn.addEventListener("click", function () {
      var img = btn.querySelector("img");
      openLightbox(btn.getAttribute("data-full"), img ? img.alt : "");
    });
  });

  if (lightbox) {
    lightbox.addEventListener("click", function (event) {
      if (event.target === lightbox || event.target.classList.contains("lightbox-close")) {
        closeLightbox();
      }
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") closeLightbox();
    });
  }

  // Highlight the section currently in view
  var links = Array.prototype.slice.call(document.querySelectorAll(".mainnav a"));
  var sections = links
    .map(function (a) { return document.getElementById(a.getAttribute("href").slice(1)); })
    .filter(Boolean);

  if ("IntersectionObserver" in window && sections.length) {
    var navObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        links.forEach(function (a) {
          a.classList.toggle("active", a.getAttribute("href") === "#" + entry.target.id);
        });
      });
    }, { rootMargin: "-45% 0px -50% 0px" });
    sections.forEach(function (section) { navObserver.observe(section); });
  }
})();
