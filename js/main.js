import { setupUI } from './modules/ui.js';
import { initSoundTriggers, copyToClipboard } from './modules/utils.js';
import { initConsole, toggleConsole } from './modules/console.js';
import { checkTwitchStatus, initClipsGallery } from './modules/twitch.js';
import { initSecrets } from './modules/secrets.js';
import { initDonorsBackground } from './modules/donors.js';
import { initAuth } from './modules/auth.js';

window.copyToClipboard = copyToClipboard;
window.toggleConsole = toggleConsole;

document.addEventListener('DOMContentLoaded', () => {
    console.log(`%c DAYMON HUB %c SYSTEM ONLINE \n`, 
        'background: #f97316; color: #000; padding: 4px; font-weight: bold;', 
        'color: #f97316;'
    );

    setupUI();
    initSoundTriggers();
    initConsole();
    checkTwitchStatus();
    initClipsGallery();
    initSecrets();
    initDonorsBackground();
    initAuth();
});
