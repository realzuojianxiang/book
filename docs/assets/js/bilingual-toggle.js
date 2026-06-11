/* ============================================================
   Bilingual Toggle — show/hide Chinese translations
   双语切换：显示/隐藏中文译文
   ============================================================ */
(function () {
  'use strict';

  const STORAGE_KEY = 'eyawkmath-bilingual-mode';

  // Create toggle buttons
  function createToggle() {
    const container = document.createElement('div');
    container.className = 'bilingual-toggle';

    const btnBoth = document.createElement('button');
    btnBoth.innerHTML = '🔤 双语';
    btnBoth.title = '显示中英双语';

    const btnEn = document.createElement('button');
    btnEn.innerHTML = '🇬🇧 EN';
    btnEn.title = '仅显示英文原文';

    const btnZh = document.createElement('button');
    btnZh.innerHTML = '🇨🇳 中文';
    btnZh.title = '仅显示中文译文';

    container.append(btnBoth, btnEn, btnZh);
    document.body.appendChild(container);

    // Restore saved state
    const saved = localStorage.getItem(STORAGE_KEY) || 'both';
    applyMode(saved, btnBoth, btnEn, btnZh);

    // Event listeners
    btnBoth.addEventListener('click', () => applyMode('both', btnBoth, btnEn, btnZh));
    btnEn.addEventListener('click', () => applyMode('en', btnBoth, btnEn, btnZh));
    btnZh.addEventListener('click', () => applyMode('zh', btnBoth, btnEn, btnZh));
  }

  function applyMode(mode, btnBoth, btnEn, btnZh) {
    localStorage.setItem(STORAGE_KEY, mode);
    document.body.classList.remove('hide-translations', 'hide-english');

    btnBoth.classList.remove('active');
    btnEn.classList.remove('active');
    btnZh.classList.remove('active');

    if (mode === 'en') {
      document.body.classList.add('hide-translations');
      btnEn.classList.add('active');
    } else if (mode === 'zh') {
      document.body.classList.add('hide-english');
      btnZh.classList.add('active');
    } else {
      btnBoth.classList.add('active');
    }
  }

  // Initialize on DOM ready
  document.addEventListener('DOMContentLoaded', createToggle);

  // Support instant navigation (MkDocs Material SPA mode)
  document$.subscribe(function () {
    if (!document.querySelector('.bilingual-toggle')) {
      createToggle();
    }
  });
})();
