// ==========================
// MOBILE MENU TOGGLE
// ==========================
const navbar = document.querySelector(".navbar");
const menuToggle = document.getElementById("menuToggle");

if (menuToggle) {
  menuToggle.addEventListener("click", () => {
    navbar.classList.toggle("open");
  });
}

document.querySelectorAll(".navbar a").forEach(link => {
  link.addEventListener("click", () => {
    navbar.classList.remove("open");
  });
});

// ==========================
// ACTIVE NAVIGATION ON SCROLL
// ==========================
const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll(".navbar a");

window.addEventListener("scroll", () => {
  let current = "";

  sections.forEach(section => {
    const sectionTop = section.offsetTop - 160;
    const sectionHeight = section.offsetHeight;

    if (window.scrollY >= sectionTop && window.scrollY < sectionTop + sectionHeight) {
      current = section.getAttribute("id");
    }
  });

  navLinks.forEach(link => {
    link.classList.remove("active");
    if (link.getAttribute("href") === "#" + current) {
      link.classList.add("active");
    }
  });
});

// ==========================
// STICKY NAVBAR SHADOW
// ==========================
const header = document.querySelector(".header");

window.addEventListener("scroll", () => {
  header.style.boxShadow = window.scrollY > 60
    ? "0 6px 20px rgba(0,0,0,.35)"
    : "none";
});

// ==========================
// SCROLL REVEAL ANIMATION
// ==========================
const revealTargets = document.querySelectorAll(
  "section, .card, .project, .skill, .contact-item, .cert-list li"
);

revealTargets.forEach(el => el.classList.add("reveal"));

const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("in");
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.15 });

revealTargets.forEach(el => revealObserver.observe(el));

// ==========================
// TYPING EFFECT
// ==========================
const roles = [
  "AI & Product Manager",
  "Web Developer",
  "Entrepreneur",
  "Problem Solver"
];

let roleIndex = 0;
let charIndex = 0;
const typedEl = document.querySelector(".typed");

function typeRole() {
  if (!typedEl) return;

  const current = roles[roleIndex];

  if (charIndex <= current.length) {
    typedEl.textContent = current.slice(0, charIndex);
    charIndex++;
    setTimeout(typeRole, 80);
  } else {
    setTimeout(eraseRole, 1400);
  }
}

function eraseRole() {
  const current = roles[roleIndex];

  if (charIndex > 0) {
    typedEl.textContent = current.slice(0, charIndex);
    charIndex--;
    setTimeout(eraseRole, 40);
  } else {
    roleIndex = (roleIndex + 1) % roles.length;
    setTimeout(typeRole, 300);
  }
}

typeRole();

// ==========================
// BACK TO TOP BUTTON
// ==========================
const topBtn = document.createElement("button");
topBtn.innerHTML = "&uarr;";
topBtn.id = "topBtn";
topBtn.setAttribute("aria-label", "Back to top");
document.body.appendChild(topBtn);

window.addEventListener("scroll", () => {
  topBtn.style.display = window.scrollY > 500 ? "block" : "none";
});

topBtn.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});

// ==========================
// CURRENT YEAR IN FOOTER
// ==========================
const footerText = document.querySelector("footer p");
if (footerText) {
  footerText.innerHTML = `&copy; ${new Date().getFullYear()} Pransu Soni. All rights reserved.`;
}

// ==========================
// CONSOLE MESSAGE
// ==========================
console.log("%cWelcome to Pransu Soni's portfolio!", "color:#00abf0;font-size:16px;font-weight:bold;");