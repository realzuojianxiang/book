/* ============================================================
   Reading Progress Bar — tracks scroll position per page
   阅读进度条 — 跟踪每页滚动位置
   ============================================================ */
(function () {
  'use strict';

  const PROGRESS_KEY = 'eyawkmath-reading-progress';

  // Create progress bar element
  function createProgressBar() {
    const bar = document.createElement('div');
    bar.className = 'reading-progress';
    bar.style.width = '0%';
    document.body.appendChild(bar);
    return bar;
  }

  // Update progress bar width based on scroll position
  function updateProgress(bar) {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    bar.style.width = Math.min(progress, 100) + '%';
  }

  // Save reading progress for current page
  function saveProgress() {
    const path = window.location.pathname;
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = docHeight > 0 ? scrollTop / docHeight : 0;

    try {
      const data = JSON.parse(localStorage.getItem(PROGRESS_KEY) || '{}');
      data[path] = {
        progress: progress,
        timestamp: Date.now()
      };
      // Keep only last 100 entries
      const keys = Object.keys(data);
      if (keys.length > 100) {
        keys.sort((a, b) => data[a].timestamp - data[b].timestamp);
        keys.slice(0, keys.length - 100).forEach(k => delete data[k]);
      }
      localStorage.setItem(PROGRESS_KEY, JSON.stringify(data));
    } catch (e) {
      // localStorage quota exceeded — ignore
    }
  }

  // Restore scroll position for current page
  function restoreProgress() {
    try {
      const data = JSON.parse(localStorage.getItem(PROGRESS_KEY) || '{}');
      const path = window.location.pathname;
      if (data[path] && data[path].progress > 0.05) {
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        window.scrollTo(0, data[path].progress * docHeight);
      }
    } catch (e) {
      // Ignore errors
    }
  }

  // Initialize
  document.addEventListener('DOMContentLoaded', function () {
    const bar = createProgressBar();

    // Throttled scroll handler
    let ticking = false;
    window.addEventListener('scroll', function () {
      if (!ticking) {
        requestAnimationFrame(function () {
          updateProgress(bar);
          ticking = false;
        });
        ticking = true;
      }
    });

    // Save progress on scroll stop and page unload
    let saveTimeout;
    window.addEventListener('scroll', function () {
      clearTimeout(saveTimeout);
      saveTimeout = setTimeout(saveProgress, 500);
    });
    window.addEventListener('beforeunload', saveProgress);

    // Initial update
    updateProgress(bar);
  });

  // Support MkDocs Material SPA navigation
  document$.subscribe(function () {
    restoreProgress();
  });
})();
