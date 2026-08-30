# 🎮 Ayaneo Pocket Air Mini: Zero to Hero Setup Guide

Welcome to the ultimate guide for transforming your Ayaneo Pocket Air Mini (PAM) into a high-performance retro gaming powerhouse. This guide covers everything from the initial unboxing to "Dark Arts" system optimizations.

---

### ☕ Support My Work
If this guide saves you hours of frustration and helps you build your dream handheld, consider buying me a coffee!

<a href="https://www.buymeacoffee.com/cyberyellowninja" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

<a href="https://ko-fi.com/cyberyellowninja" target="_blank">
  <img src="https://storage.ko-fi.com/cdn/kofi5.png?v=3"
       alt="Buy Me a Coffee at ko-fi.com"
       style="height: 60px !important; width: 217px !important;"></a>
       
---

## 📋 Table of Contents

1. [🛠️ Phase 1: Preparation & Materials](#phase-1-preparation--materials)
2. [💾 SD Card Setup & Format](#sd-card-setup--format)
3. [🍳 Phase 2: Mixing the Ingredients](#phase-2-mixing-the-ingredients)
4. [📂 Phase 3: Finding Your Library](#phase-3-finding-your-library)
5. [🎨 Phase 4: ES-DE Initial Setup & Folders](#phase-4-es-de-initial-setup--folders)
6. [⚙️ Phase 5: Emulator Configuration](#phase-5-emulator-configuration)
7. [🎨 Phase 6: ES-DE Advanced Setup & Scraping](#phase-6-es-de-advanced-setup--scraping)
8. [⚡ Phase 7: System Optimization & Battery Health](#phase-7-system-optimization--battery-health)
9. [⚡ Phase 7.5: Performance & Audio Optimization Profiles](#phase-75-performance--audio-optimization-profiles)
10. [🥷 Phase 8: The Dark Arts](#phase-8-the-dark-arts)
11. [📱 Phase 9: Removing Touch Overlays](#phase-9-removing-touch-overlays)
12. [🚀 Phase 10: Alternative OS: GammaOS](#phase-10-alternative-os-gammaos)
13. [📜 Appendix: Must-Play Games per System](#appendix-must-play-games-per-system)
14. [🤝 Community Contributions & Credits](#community-contributions--credits)

> [!NOTE]
> Use the links above to jump directly to any section.

---

## 🛠️ Phase 1: Preparation & Materials

<span>🟢 Beginner</span>

Before we begin, ensure you have the following ready:
* **The Device:** Ayaneo Pocket Air Mini (charged to at least 60%).
* **Storage:** A high-quality MicroSD card (128GB to 512GB+ recommended). See [SD Card Setup](#sd-card-setup--format) below for format and mount guidance.
* **Software:** Download these apps from the Play Store or their official sites:
  * **Frontend:** ES-DE (EmulationStation Desktop Edition)
  * **File Managers:** MiXplorer or ZArchiver
  * **Torrent Manager:** Flud
  * **Editors:** QuickEdit
  * **System Tools:** AccuBattery, Shizuku, Termux
  * **Emulators:** RetroArch, Dolphin, NetherSX2, PPSSPP, Duckstation, Azahar, MelonDS, Mupen64Plus FZ.

---

## 💾 SD Card Setup & Format

<span>🟢 Beginner</span>

Your SD card stores all ROMs, BIOS files, emulator configs, and save states. Getting this right upfront saves pain later.

### Which format: exFAT or FAT32?

| Format | Pros | Cons |
|--------|------|------|
| **exFAT** (recommended) | No 4GB file limit — works with PS2, GC, and Wii ISOs without splitting | Slightly less compatible with some USB adapters and very old devices |
| **FAT32** | Maximum compatibility across devices and operating systems | 4GB file size limit — ROMs larger than 4GB must be split or you must use a tool to split them |

**Use exFAT** if you play PS2, GameCube, or Wii games (ISOs often exceed 4GB). Use FAT32 only if you only play PS1, N64, PSP, Genesis, SNES, and smaller ROMs — or if you need the SD card to work across maximum devices.

### Mount: External storage, not adoptable storage

Always use your SD card as **external portable storage** — not as internal adoptable storage. The difference:
- **External (portable):** The SD card shows up as removable media. ES-DE points to folders on it. If you swap cards, you keep your system settings.
- **Adoptable (internal):** Android encrypts and ties the SD card to your device. You lose it if you format, and it is harder to back up.

The guide's ES-DE setup uses the external approach: `SD Card > ES-DE`, `SD Card > ROMS`. This is intentional.

### Quick setup checklist

1. Format the SD card as exFAT using your PC or the Ayaneo settings
2. Create these folders on the SD card: `ES-DE`, `ROMS`, `BIOS`, `Saves`, `Save States`
3. In ES-DE, set **Data Directory** to `SD Card > ES-DE` and **ROMs Directory** to `SD Card > ROMS`
4. Point RetroArch and other emulators to the SD card folders for saves and states

### 🎮 Button Naming Reference

The guide uses standard gaming controller terminology. Here is a quick reference for the Pocket Air Mini:

| Name | Location | Used for in this guide |
|------|----------|----------------------|
| L1 / R1 | Top-left / Top-right shoulder buttons (top bumpers, light press) | Quick actions, Wii extension mapping |
| L2 / R2 | Bottom-left / Bottom-right triggers (deep press) | Fast-forward (RetroArch), slow-mo, analog triggers |
| L3 / R3 | Click down on the left / right analog stick | RetroArch hotkey enable (L3+R3 opens menu), in-game functions |

> [!TIP]
> When the guide mentions pressing **L3** or **R3**, it means clicking the analog sticks down until you feel a click — the sticks themselves are buttons on the Pocket Air Mini.

---

## 🍳 Phase 2: Mixing the Ingredients (The Recipe for Success)

<span>🟢 Beginner</span>

### **1. System & Firmware Updates**
Ensure the "brain" of your device is up to date.
1. Open the **System Update** app. Install all updates and **Restart**.
2. Open the **Ayasettings** app. Perform the internal update and **Restart** again.

### **2. Virtual Memory Booster**
Crucial for heavy systems like PS2 or Switch:
1. Open **Ayasettings**.
2. Go to **Device -> Virtual Memory Management**.
3. Set the value to **3GB** and enable the **Swap** switch below it.

> [!NOTE]
> **2GB vs 3GB:** The guide recommends 3GB virtual memory for all configurations. If you only play systems up to and including PS1, N64, PSP, and Genesis, 2GB *may* be sufficient. Anything above PS1 (PS2, GC, Wii) or running multiple emulators simultaneously benefits significantly from the 3GB setting. When in doubt, leave it at 3GB.

### **3. Setting up Flud (The Download Manager)**
1. Open **Flud** and grant permissions.
2. Tap the Menu (top left) -> Select **SD Card**.
3. Navigate to the `Downloads` folder.
4. Tap the **"+" folder icon** (top right), name it `Flud`, and select **"Use this folder"**.

---

## 📂 Phase 3: Finding Your Library (The Directions)

<span>🟢 Beginner</span>

I cannot provide direct links, but I can show you the way.

* **The Starter Pack:** Search Google for **"tiny best set: go! archive"**.
  * Look for the **94 GB** version.
  * Download the **Torrent file** from the bottom of the page and open it with Flud.
* **The Holy Grail:** Remember the keyword **"Megathread"**. It is the paradise for retro gamers looking for specific console ROMs and BIOS files.

---

## 🎨 Phase 4: ES-DE Initial Setup & Folders

<span>🟡 Intermediate</span>

1. Open **ES-DE**.
2. **Data Directory:** Select your **SD Card** -> Create folder `ES-DE` -> Select **"Use this folder"**.
3. **ROMs Directory:** Select your **SD Card** -> Create folder `ROMS` -> Select **"Use this folder"**.
4. Tap **"Create them"**, then **"I understand"**. Once finished, **fully close** the app.

### **Organizing BIOS & ROMs**
Using **ZArchiver**, navigate to your downloaded `tiny set best go-games`:
1. **BIOS:** Copy everything from the `bios` folder and the `expansion-64` folder inside the zip to the `BIOS` folder on your **SD Card**.
2. **ROMs:** Move game files into their corresponding folders inside the `ROMS` directory on your SD card. 
3. **Pro Tip:** Delete the zip files after extraction to save space!


> [!NOTE]
> **Daijishō as Default Launcher — After Firmware Updates:** If you use Daijishō as your default launcher and receive a firmware update from Ayaneo, the update process may reset your default launcher to the stock Ayaneo launcher. After any firmware update, go to **Settings → Apps → Default Apps → Home App** and re-select Daijishō. *Source: reported — known Android behavior pattern, PAM-specific confirmation pending.*
## ⚙️ Phase 5: Emulator Configuration (The Pro Setup)

<span>🟡 Intermediate</span>

### **1. RetroArch (Multi-System Hub)**
Open RetroArch and grant permissions.
* **Visuals:** Settings > User Interface > On-Screen Notifications > Scale Graphics Widgets Automatically: **OFF** | Graphics Widgets Scale Override: **0.75x**.
* **Controls:** Settings > Input > Retropad Binds > Port 1 > Analog to Digital Type: **Left Analog**.
* **Hotkeys (L3 as Enable Button):**
    * Menu Toggle: **L3 + R3** | Quit: **Start + L1** | Fast Forward: **R2** | Slow Motion: **L2**.
    * **Save State: R1** | **Load State: L1** | Screenshots: **Y**.
* **Directories:** Settings > Directory. Point **System/BIOS**, **Saves**, and **Save States** to their respective folders on your **SD Card**.
* **Speed Hack:** Open `Android/data/com.retroarch.aarch64/files/retroarch.cfg` with **QuickEdit**. Add `input_threaded = "false"` at the bottom.
* **Shaders:** Use `LCD-Grid-V2` for Handhelds and lightweight CRT shaders for TV consoles. Avoid "Mega Bezel".

> [!TIP]
> CRT-style shaders can look very accurate but may be heavier depending on the preset.
>
> For demanding systems (N64 / Dreamcast), consider using:
> - CRT-Lottes-fast
> - Lightweight shaders
>
> Performance should take priority over visual effects on heavier platforms.

#### 🎨 Community Shader Recommendations (Optional)

If you want to experiment beyond the default presets:

**General CRT Options**
- `crt-geom-mini` → Lightweight, great overall look  
- `crt-geom` → Better image quality (uses more power)  
- `zfast-crt-composite` → Excellent for Genesis / Mega Drive  
- `zfast-crt-svideo` → Softer, blurrier authentic CRT look  
- `crt-pi` → Makes arcade titles pop while remaining lightweight  

**3D Systems**
- `crt-newpixie-mini` → Recommended for PS1 and other early 3D systems  

**Handheld Systems**
- **GBA:** `quilez interpolation` + `lcdx3`  
- **Game Boy DMG:** `gb-palette` + `lcdx3`  
- **Game Boy Color:** `pixel transparency` + `lcdx3`  

> These are visual preference options and may slightly impact performance.

### **2. Dolphin (GameCube & Wii)**
* **Paths:** Add `SD Card > ROMS > GC` and `Wii` folders.
* **Graphics:**
    * Video Backend: **Vulkan**
    * Shader Compilation: **Skip Drawing (ON)** | **Compile Shaders Before Starting (ON)**
    * Internal Resolution: **2x Native**
* **Enhancements:**
    * Anti-Aliasing: **OFF** | Anisotropic Filtering: **2x ή OFF**
    * Scaled EFB Copy: **ON** | Per-Pixel Lighting: **OFF** | Force Texture Filtering: **OFF**
* **Hacks:**
    * Skip EFB Access from CPU: **ON** | Ignore Format Changes: **ON**
    * Store EFB Copies to Texture Only: **ON** | Defer EFB Copies to RAM: **ON**
* **Performance / CPU:**
    * Dual Core: **ON** | Emulated CPU Clock Speed: **60% – 70%** 
* **Advanced:**
    * Backend Multithreading: **ON** | Shader Cache: **ON** | V-Sync: **OFF**
   
> [!TIP]
> **Mario Kart: Double Dash Blue Overlay Fix:** If you experience a blue overlay during gameplay, it is a Vulkan/EFB quirk on the Mali-G76 GPU. The standard fix is to go to **Dolphin Hacks** and set **"Store EFB Copies to Texture Only"** to **OFF**. If that doesn't resolve it, the definitive fix is to switch the graphics **Backend** from Vulkan to **OpenGL** in `Dolphin > Graphics > General`. The compatibility table rates this game **A (OpenGL if Vulkan EFB issues)** — this is exactly that case. If both settings fail, a cold-reboot (full shutdown, not restart) can clear persistent EFB state.

* **Wii Controls (FPS Setup):** Extension: **Classic**. Map ZL/ZR to L1/R1 and Triggers to L2/R2.

  ---

## 🔧 Community Contribution – Dolphin Enhancement Notes

Additional refinement based on community testing.

### Arbitrary Mipmap Detection

Enable this **only if** you notice:

- Texture shimmer
- Flickering textures
- Surfaces that appear overly sharp or “sparkly” during movement

These issues can occur in certain titles due to missing mipmap detection in Vulkan.

**Fix:**

Dolphin → Graphics → Enhancements  
→ Enable **Arbitrary Mipmap Detection**

⚠️ Leave this OFF by default.  
It may slightly impact performance and is not needed for most games.

---

### Updated Guidance

Default Recommendation:
- Keep **Arbitrary Mipmap Detection = OFF**

Conditional Use:
- Enable only when visual artifacts appear.

This preserves performance-first behavior while allowing targeted visual correction when needed.


### **3. NetherSX2 (PlayStation 2)**
* **BIOS:** Import from `SD Card > BIOS`.
* **Graphics:**
    * Renderer: **Vulkan**
    * Threaded Presentation: **ON**
    * Blending Accuracy: **Basic**
    * Mipmapping: **Automatic**
* **System (Underclocking):**
    * EE Cycle Rate: **75% (-1)**
    * EE Cycle Skip: **1 (Mild Skip)**
    * Multi-threaded VU1: **ON**
    * Instant VU1: **OFF**
    * Fast CDVD: **ON**
* **Speedhacks:**
    * INTC Spin Detection: **ON**
    * Wait Loop Detection: **ON**
    * mVU Flag Hack: **ON**
* **Controls:** Controller Port 1 > Automatic Mapping.

#### 🎮 Game-Specific Optimization: Fatal Frame Series

Fatal Frame titles are among the most demanding PS2 games on the Pocket Air Mini due to heavy post-processing and alpha effects.

Use the following tested combo for stable performance:

##### Graphics
- Renderer: Vulkan  
- Blending Accuracy: Basic  
- Mipmapping: Automatic  

##### System
- EE Cycle Rate: 75% (-1)  
- EE Cycle Skip: 1 (Mild Skip)  
- Multi-threaded VU1: ON  

##### Speedhacks
- INTC Spin Detection: ON  
- Wait Loop Detection: ON  
- mVU Flag Hack: ON  

##### Advanced (Performance Boost)
- Disable Depth Emulation: ON  
- GPU Palette Conversion: OFF  

This combo reduces GPU overhead while preserving visual integrity in gameplay-heavy scenes.

> Note: Minor slowdowns may still occur during intense camera effects — this is expected.

### **4. PPSSPP (PSP)**
* **Graphics:** Backend: **Vulkan** | Rendering Resolution: **2x** | Frame Skipping: **1** | Auto Frameskip: **ON**.
* **Performance:** Lazy Texture Caching: **ON** | Fast Memory: **OFF** | Ignore Bad Memory Accesses: **ON**.

### **5. Duckstation (PS1)**
* **Graphics:** Renderer: **Vulkan** | Resolution Scale: **3x or 4x** | PGXP Operation Mode: **Memory Only** (fixes wobbly textures).
* **Controller:** Set Touchscreen View to **None**.

### **6. Azahar (3DS)**
* **Graphics:** API: **Vulkan** | Resolution: **3x (lighter titles) / 2x (heavier titles)**.
* **Performance:** Async Shader Compilation: **Enabled** | Disk Shader Cache: **Enabled** | Accurate Multiplication: **Disabled**.
* **Mapping:** Screen Swap: **L3** | Cycle Layout: **R3**.

### **7. MelonDS (DS) & Mupen64Plus FZ (N64)**
* **MelonDS:** Set Resolution to **2x/3x**. Map Screen Swap to **L3**.
* **Mupen64Plus FZ:** Use **GLideN64-Very-Accurate** profile. Map **C-Buttons** to the **Right Analog Stick**.

## 🎨 Phase 6: ES-DE Advanced Setup & Scraping

<span>🟡 Intermediate</span>

Make your collection look professional and set ES-DE as your permanent home.

1. **Interface:** Start Menu > UI Settings > Theme Downloader. Download **"Art Book Next"**.
2. **Scraper (Game Art):**
   * Register for free at [screenscraper.fr](https://www.screenscraper.fr/).
   * Enter credentials in **Scraper > Account Settings**.
   * Select your desired metadata (Box art, screenshots, etc.).
   * Set **Region** and **Language**.
   * **Start Scraping:** This may take several hours. It is recommended to run this overnight.
3. **App Integration:** * Utilities > Game Importer > Import to System: **Android Apps**.
   * Select your installed apps (Flud, Chrome, etc.) and Import.
   * Repeat for **Emulators** to have quick access to standalone apps.
4. **Default Launcher:** * Android Settings > Apps & Notifications > Default Apps > Home App.
   * Select **ES-DE**.

---

> [!NOTE]
> Standalone emulators are intended to be launched directly from ES-DE system tabs.
> The separate Emulators tab exists only for configuration and maintenance.
>
> To launch games directly:
> Start → Other Settings → Alternative Emulators
> Assign your standalone emulator per system.

## ⚡ Phase 7: System Optimization & Battery Health

<span>🟡 Intermediate</span>

### **1. Developer Performance Tweaks**
Go to **Settings > System > Developer Options**:
* **Window/Transition/Animator Scale:** Set all to **0x (Off)**.
* **Background Process Limit:** Set to **2**.
* **Play Protect:** Disabled. In **Google Play Store → Profile → Play Protect → Settings**, turn off **Scan apps with Play Protect**. Install your trusted apps before disabling.
* **Location Services:** Disabled. Go to **Settings → Location** and turn off Location. Also disable Wi-Fi and Bluetooth scanning.
* **Auto-Sync:** Disabled. Go to **Settings → Accounts** and turn off **Automatically sync app data**.
* **Logging:** Disabled. Search Settings for **Logger Buffer Size** and turn it off.
* **Disable HW Overlays:** **ON**.

> [!NOTE]
> **Hardware Overlays — Community Conflict:** The Dark Arts approach recommends disabling hardware overlays for better GPU performance. However, uriuri89 (BruhMeh guide) reports that keeping hardware overlays enabled has **no measurable performance benefit** in testing and may increase GPU rendering overhead in some cases.
>
> **Current guidance:** The guide defaults to the Dark Arts approach (disable HW overlays). If you experience issues or want to test both: toggle this setting, run your target emulator for 5–10 minutes, and compare. Either setting can be correct depending on your specific unit, firmware version, and emulator. If in doubt, try both and keep whichever works better.

> [!NOTE]
> On Android 11, Background Process Limit resets after a full shutdown (cold boot).  
> Sleep mode does not reset it.  
> If you power the device off completely, you will need to set it again.

### **2. Battery Health (AccuBattery)**
1. Open **AccuBattery**.
2. Set the **Charge Alarm to 80%**.
3. Always unplug at 80% to maximize the lifespan of your PAM's internal battery.

> [!WARNING]
> **Screen Ghosting — Known PAM Hardware Characteristic:** Some Pocket Air Mini units exhibit visible ghosting or motion blur on the 4.2" display, particularly with retro games that have fast-moving elements or high-contrast visuals. This is a hardware panel characteristic — no settings fix it. If ghosting is distracting, try slightly reducing emulator speed (RetroArch: Fast Forward → ~1.5x) to reduce perceived motion blur. *Sources: r/SBCGaming, retrohandhelds.gg.*

---

---

## 🚀 Phase 7.5: Performance & Audio Optimization Profiles

<span>🟠 Advanced</span>
### AYASpace Quick Menu (IO Button)

If your PAM has the AYASpace app installed, pressing the **IO button** (the small button on the side of the device) opens the AYASpace quick menu at any time — even in-game. From here you can:
- Switch performance profiles (gaming, balanced, battery saver)
- Adjust fan speed manually
- Access the device equalizer

This is a fast way to tweak performance or fan settings without leaving your game. The guide's Phase 7.5 profiles cover the equivalent settings for users who don't have AYASpace or prefer manual configuration.

> [!NOTE]
> The IO button behavior depends on your current firmware and AYASpace version. If the quick menu doesn't appear, check that AYASpace is installed and up to date.


This section applies calibrated thermal and audio tuning for stable high-performance operation on the Ayaneo Pocket Air Mini.

---

### 🔥 1. Thermal Profile — Custom Fan Curve

**Objective:** Maintain sustained performance under load while keeping acoustic output controlled.

| Temperature (°C) | Fan Speed (%) |
|------------------|---------------|
| 0–45             | 25            |
| 55               | 40            |
| 65               | 60            |
| 75               | 80            |
| ≥83              | 100           |

**Apply:**  
AYASpace → Fan Settings → Custom → Drag points exactly as shown → Save

---

### 🔊 2. Audio Profile — Master EQ v1.3

**Objective:** Improve clarity and perceived bass response on integrated downward-firing speakers while maintaining safe headroom.

#### 10-Band Graphic EQ

| Frequency | Gain (dB) |
|-----------|-----------|
| 31 Hz     | 0.0       |
| 62 Hz     | +2.5      |
| 125 Hz    | +3.0      |
| 250 Hz    | +1.5      |
| 500 Hz    | -1.5      |
| 1K Hz     | 0.0       |
| 2K Hz     | +2.5      |
| 4K Hz     | +3.0      |
| 8K Hz     | +2.0      |
| 16K Hz    | +1.0      |

#### Global Parameters
- **Input Gain:** -2.0 dB  
- **Bass Gain:** +4.0 dB @ 120 Hz  

**Apply:**  
Equalizer → "+" → Create preset → Name: `Master EQ v1.3` → Enter values → Confirm

> Recommended for 70–85% volume range.  
> Reduce Bass Gain slightly for extended near-maximum volume sessions.

> [!NOTE]
> Some Android 11 firmware builds do not automatically re-apply EQ presets after a full shutdown.
> You may need to manually re-enable the preset after reboot.
---

### ✔ Validation Checklist

After applying both profiles:

- Fan ramps progressively under load  
- No sudden full-speed spikes during light gaming  
- No audible distortion during heavy scenes  
- Clear mids and highs without harshness  
- Stable thermals during extended play sessions  

---

## 🥷 Phase 8: The Dark Arts (System Debloating)

<span>🔴 Advanced</span>
This stage will disable unnecessary system background processes to free up RAM and CPU cycles. We will use **Shizuku**, **QuickEdit**, and **Termux**.

#### 1. Setup Shizuku
1. Open **Shizuku**.
2. Tap **Start via Wireless Debugging**.
3. Go to **Developer Options** > Enable **Wireless Debugging** > Tap **Allow**.
4. Tap on the "Wireless Debugging" text, then **Pair device with pairing code**.
5. Enter the code into the Shizuku notification to pair.
6. Go back to Shizuku and tap **Start**. You should see "Shizuku is running".

#### 2. Configure Rish for Termux
1. In Shizuku, tap **Use Shizuku in Terminal** and select **Export files**.
2. Save the files to your SD card in a folder named `Ter` (e.g., `SD Card > Ter`).
3. Open **QuickEdit** and grant the necessary permissions.
4. Tap the three lines (menu) and navigate to `SD Card > Ter > rish`.
5. On **Line 24**, find the variable `"PKG"` and change it to:
   `"com.termux"`
6. Tap the **Disk icon** (Save) and then the **X** to close the file.


#### 3. Run the Debloater in Termux
1. Open **Termux**.
2. Type `cd /storage` and press **Enter**.
3. Type `ls` and press **Enter**. Note your SD card's ID (e.g., `1234-ABCD`).
4. Navigate to your folder (replace `1234-ABCD` with your ID):
   `cd /storage/1234-ABCD/Ter`
 5. Type `termux-setup-storage`
   allow access 
6. Run the rish script by typing:
   `sh rish`
7. **IMPORTANT:** A Shizuku prompt will appear. Tap **"Allow all the time"**. 
   *(Now Termux will officially show up in Shizuku's "Authorized applications" list).*
8. After granting permission, **Copy and Paste** the following block to disable the bloatware:

```bash
pm disable-user --user 0 com.android.dreams.basic
pm disable-user --user 0 com.android.egg
pm disable-user --user 0 com.android.wallpaper.livepicker
pm disable-user --user 0 com.android.wallpaperbackup
pm disable-user --user 0 com.android.traceur
pm disable-user --user 0 com.google.android.feedback
pm disable-user --user 0 com.google.android.printservice.recommendation
pm disable-user --user 0 com.google.android.onetimeinitializer
pm disable-user --user 0 com.google.android.apps.restore
pm disable-user --user 0 com.google.android.ims
pm disable-user --user 0 com.mediatek.engineermode
pm disable-user --user 0 com.mediatek.mtklogger
pm disable-user --user 0 com.mediatek.gnssdebugreport
pm disable-user --user 0 com.mediatek.batterywarning
```
9. **​Restart your device. You will notice improved battery life and more stable performance due to reduced background CPU activity.**

## 🧹 Additional Debloat List (Optional)

Safe to disable on a gaming-only device.  
Do **NOT** apply if you use enterprise features, contact/calendar sync, MIDI, or advanced networking.

### Disable via Termux:
```bash
pm disable-user --user 0 com.android.pacprocessor  
pm disable-user --user 0 com.android.proxyhandler  
pm disable-user --user 0 com.android.carrierconfig  
pm disable-user --user 0 com.android.ons  
pm disable-user --user 0 com.android.simappdialog  
pm disable-user --user 0 com.google.android.syncadapters.contacts  
pm disable-user --user 0 com.google.android.syncadapters.calendar  
pm disable-user --user 0 com.android.managedprovisioning  
pm disable-user --user 0 com.google.mainline.telemetry  
pm disable-user --user 0 com.android.bluetoothmidiservice  
pm disable-user --user 0 com.android.soundpicker  
pm disable-user --user 0 com.android.music  
pm disable-user --user 0 com.android.providers.partnerbookmarks
```

### ♻ Undo Debloat (Restore Disabled Packages)

If something stops working after debloating, you can restore any removed system package.

#### Command:
```
pm enable package.name
```

#### Example:
```
pm enable com.google.android.ims
```

> Reboot the device after restoring any package.

> [!NOTE]
> Debloating is persistent.
> Disabled packages remain disabled across reboots.
>
> They will only return if:
> - A factory reset is performed
> - A system update replaces them
> - You manually re-enable them
>
> Root is not required.
>
> Debloating mainly improves long-session stability rather than raw FPS.
> If your system is already stable, this phase is optional.
### 3. Google Play Services Hardening

After disabling packages with Canta, further reduce Google Play Services background activity with these ADB commands. Run these after the Canta debloating steps.

**Reduce GMS background activity:**

> [!SOURCE]
> Commands from [BruhMeh PAM Stock OS Optimization Guide](https://github.com/BruhMeh/PAM-Stock-OS-Optimization-Guide), §04-01 & §04-02

```bash
adb shell cmd appops set com.google.android.gms RUN_IN_BACKGROUND ignore
adb shell am set-standby-bucket com.google.android.gms restricted
```

**Reduce Play Store background activity:**

> [!SOURCE]
> Commands from [BruhMeh PAM Stock OS Optimization Guide](https://github.com/BruhMeh/PAM-Stock-OS-Optimization-Guide), §04-01 & §04-02

```bash
adb shell cmd appops set com.android.vending RUN_IN_BACKGROUND ignore
adb shell am set-standby-bucket com.android.vending restricted
```

**Restrict Gboard:**

> [!SOURCE]
> Commands from [BruhMeh PAM Stock OS Optimization Guide](https://github.com/BruhMeh/PAM-Stock-OS-Optimization-Guide), §04-01 & §04-02

```bash
adb shell cmd appops set com.google.android.inputmethod.latin RUN_IN_BACKGROUND ignore
adb shell am set-standby-bucket com.google.android.inputmethod.latin restricted
```

**Block OTA updater from running in background:**

> [!SOURCE]
> Commands from [BruhMeh PAM Stock OS Optimization Guide](https://github.com/BruhMeh/PAM-Stock-OS-Optimization-Guide), §04-01 & §04-02

```bash
adb shell cmd appops set com.ayaneo.update RUN_IN_BACKGROUND ignore
adb shell am set-standby-bucket com.ayaneo.update restricted
```

> [!NOTE]
> These commands restrict background activity only — Google Play Store still updates apps normally. These are among the highest-impact optimizations for idle battery and background CPU.

### 4. Troubleshooting Common Issues

**Google Play Services errors after debloating:**
If you see Play Services errors, re-enable the specific package via Canta. Run the AppOps commands above to fine-tune without fully re-enabling `com.google.android.gms`.

**Play Store won't update apps:**
Verify `com.android.vending` is not fully disabled. Re-enable and re-run the AppOps commands if needed.

**Emulator performance issues after debloating:**
Re-run AOT compilation to re-optimize affected emulators:

> [!SOURCE]
> Commands from [BruhMeh PAM Stock OS Optimization Guide](https://github.com/BruhMeh/PAM-Stock-OS-Optimization-Guide), Appendix B

```bash
adb shell cmd package compile -m speed -a
```

Or compile a single emulator:

```bash
adb shell cmd package compile -m speed -f <package_name>
```

**After a firmware reset:**
Re-run the Canta steps and the ADB commands above after any firmware update. Updates can restore disabled packages and reset App Standby buckets.

### 5. Automated Scripts (Optional — Advanced Users)

For automated RetroArch installation, shader configuration, and first-run optimization, see the **Ayaneo Handheld Scripts** collection by BruhMeh:

→ [github.com/BruhMeh/Ayaneo-Handheld-Scripts](https://github.com/BruhMeh/Ayaneo-Handheld-Scripts)

Includes: automated RetroArch nightly + cores + shaders, performance tuning scripts, and display refresh rate optimization. Use these to automate the setup instead of configuring manually.


## 📱 Phase 9: Removing Touch Overlays

<span>🟢 Beginner</span>

Standalone emulators often enable touch icons by default, which can be distracting on a controller-first handheld.  
Use the following paths to hide them for a clean, console-like experience:

- **Dolphin (GC/Wii):** While in-game → Open menu → Overlay Controls → Toggle Controls → Unselect All
- **NetherSX2 / AetherSX2 (PS2):** Swipe left panel → Controller Settings → Touchscreen → Touchscreen Controller View → None
- **DuckStation (PS1):** Controller Settings → Auto-Hide Touchscreen Controller → ON
- **Mupen64Plus FZ (N64):** Settings → Profiles → Touchscreen → New → Name it "Hidden" → Tap screen → Exit → Set active profile to "Hidden"
- **MelonDS (DS):** Settings → Input → Show soft input → OFF
- **Azahar / Citra (3DS):** During gameplay → Swipe down → 3-dot menu → Disable Show Overlay
- **Vita3K (Vita):** Controls → Overlay → Untick “Show gamepad overlay ingame”
- **Yaba Sanshiro 2 (Saturn):** Settings → Input Device → Edit On-Screen Pad → Set Transparency to 0

### 💡 Pro Tip: Speed up ES-DE Startup

1. Go to **UI Settings** > **Theme Configuration**.
2. Set **Enable Theme Variant Triggers** to **Off**.
   
If your collection is massive and you want ES-DE to open instantly, you can disable the automatic startup scan:

1. Go to **ES-DE Menu** > **Other Settings**.
2. Set **Only show games from gamelist** to **On**.
   

> [!NOTE]
> If you add new games later, you must manually scan via **Menu** > **Utilities** > **Rescan ROM Directory**.

## 🚀 Phase 10 — Alternative OS: GammaOS

<span>🔴 Advanced</span>

> [!WARNING]
> **GammaOS replaces your stock OS.** Not a debloat — a full OS replacement. If you are happy with stock Android + Dark Arts (Phase 8), skip this phase entirely.
> **Prerequisite: back up your stock firmware before flashing.** Follow Ayaneo's official backup guide first. If the flash goes wrong, you need the backup to recover.

### What is GammaOS?

GammaOS is a custom Android distribution for select handheld devices that ships with a lean, gaming-focused base. It removes Ayaneo's pre-installed bloatware and replaces the stock OS entirely.

### What you get over stock + Dark Arts (v1.3.2 confirmed)

- **4K hardware video decode** — YouTube, Netflix, and streaming apps use full hardware-accelerated decoding up to 2160p (stock firmware shipped with broken HW decode, forcing software fallback with dropped frames and high CPU usage)
- **Hardware video encoding** — scrcpy and Vysor work correctly for screen mirroring and recording
- **Nano CE auto-unlock** — credential cached in device-encrypted storage; game saves and ROM data accessible on Nano boot without entering the lock screen
- **60fps boot animation** with fade-in/out and XP-style loading bar
- **System-wide equalizer (GammaEQ)** — per-profile EQ settings
- **Improved fan daemon** — refined automatic fan control behaviour vs stock
- **Refined controller defaults** — better deadzones and gamepad configuration out of the box
- **Disabled system animations** — snappier UI feel
- **Factory GPU overclock** — Mali-G76 MC4: **850 MHz → 950 MHz** (+11.8%). Benefits GPU-limited emulators (GC/Wii via Dolphin, PSP via PPSSPP at higher resolution). CPU-bound emulators (PS2 via NetherSX2) gain little from this alone.
- **Improved sleep mode** — sleep/resume fixes vs stock

> [!NOTE]
> **GammaRGB (LED control):** Performance tips in the v1.3.2 release mention disabling GammaRGB to reduce background CPU overhead. Whether LEDs are functional on your PAM unit varies — do not assume LED control is available unless your unit has addressable LEDs.

### What you lose

- Stock Ayaneo launcher and all Ayaneo-specific apps
- Google Play Services on the Full variant (Lite variant has no GApps) — install manually via Aurora Store if needed
- Official Ayaneo OTA updates
- Any Ayaneo-specific firmware optimisations

### Known issues in v1.3.2 (as of August 2026)

- **Stick drift** — reported in [GammaOS GitHub issue #338](https://github.com/TheGammaSqueeze/GammaOSNext/issues/338), not fixed in stable build
- **LT button sticking** — reported in issue #338, not fixed in stable build
- **Heating under sustained load** — no fix in stable build

### Installation

> [!CAUTION]
> GammaOS flashing has a real brick risk. Back up your stock firmware before proceeding. Do not interrupt the flash process. If you are unsure, stick with stock + Dark Arts.

1. Back up your stock firmware (Ayaneo's official backup guide)
2. Download GammaOS v1.3.2 for Pocket Air Mini from [github.com/TheGammaSqueeze/GammaOSNext](https://github.com/TheGammaSqueeze/GammaOSNext)
3. Follow the install instructions on the GammaOS GitHub (Windows + USB cable, SD card or internal storage)
4. Do a clean boot after flashing — do not restore any configs from stock OS

### After installation

- Install emulators fresh — your stock OS configs will **not** carry over
- Re-apply GammaEQ and fan settings through the GammaOS settings app
- Reconfigure ES-DE from scratch
- Consider disabling GammaRGB in Settings to reduce background CPU overhead

### Who should and shouldn't flash

**Consider GammaOS if:**
- You already run stock + Dark Arts and want to test the purpose-built alternative
- You use scrcpy or Vysor for screen mirroring or recording
- You stream 4K video and want hardware decode working properly
- You want LED/EQ/fan control without scripting (if your unit supports it)

**Stick with stock + Dark Arts if:**
- You want the simplest, lowest-risk path — stock + Dark Arts covers most of what GammaOS offers for emulation
- You rely on Ayaneo-specific apps or launcher
- You want official OTA updates
- You are new to handhelds and do not want to troubleshoot post-flash issues
- You use Google Play Services regularly (Lite variant has no GApps; Full variant has them)

### Credits

GammaOS is developed by **TheGammaSqueeze** ([GitHub](https://github.com/TheGammaSqueeze/GammaOSNext)). The Pocket Air Mini port is part of the v1.3.x release line.

---

## 📜 Appendix: Must-Play Games per System
These are curated lists of **must-have games** that run well on the Pocket Air Mini. Focus on legal backups you own. Performance tiers are based on practical testing with recommended configurations. Individual results may vary depending on scene complexity, emulator version, firmware, and device configuration.

- **Tier A**: Full speed (stable, minimal tweaks).
- **Tier B**: Minor drops (playable, some tweaks).
- **Tier C**: Playable with tweaks (demanding scenes, underclock).

**Summary:**
PS1 (DuckStation – Mostly Tier A)

| Game                  | Why Must-Play                  | Tier / Notes |
|-----------------------|--------------------------------|--------------|
| Crash Bandicoot 2/3   | Iconic platformer, fun levels | A, 3-4x res |
| Final Fantasy VII/IX  | Epic RPG story                | A, PGXP ON  |
| Resident Evil 2       | Survival horror classic       | A           |
| Castlevania: Symphony of the Night | Metroidvania masterpiece | A           |
| Metal Gear Solid      | Stealth action pioneer        | A           |
| Tony Hawk's Pro Skater 2 | Skateboarding fun            | A           |
| Parasite Eve          | Horror RPG                    | A           |

**Summary:**
PS2 (NetherSX2 – Mix A/B/C)

| Game                  | Why Must-Play                  | Tier / Notes |
|-----------------------|--------------------------------|--------------|
| God of War (1/2)      | Epic action-adventure         | B, EE -1    |
| Metal Gear Solid 3: Snake Eater | Stealth masterpiece      | B           |
| Burnout 3: Takedown   | Racing chaos                  | A           |
| Persona 4             | RPG with deep story           | B           |
| Bully                 | Open-world school adventure   | A           |
| Katamari Damacy       | Unique rolling fun            | A           |
| SSX 3                 | Snowboarding tricks           | A           |

**Summary:**
PSP (PPSSPP – Mostly A)

| Game                  | Why Must-Play                  | Tier / Notes |
|-----------------------|--------------------------------|--------------|
| God of War: Chains of Olympus | Action epic              | A, 2x res   |
| Crisis Core: Final Fantasy VII | RPG prequel             | A           |
| Persona 3 Portable    | Deep RPG/social sim           | A           |
| Metal Gear Solid: Peace Walker | Stealth co-op           | A           |
| Def Jam: Fight for NY – The Takeover | Fighting with rappers | A           |
| Jeanne d'Arc          | Tactical RPG                  | A           |
| Castlevania: The Dracula X Chronicles | Action remake  | A           |

**Summary:**
GameCube (Dolphin – Mix A/B)

| Game                  | Why Must-Play                  | Tier / Notes |
|-----------------------|--------------------------------|--------------|
| Super Smash Bros. Melee | Fighting party            | A, 2x native |
| The Legend of Zelda: Wind Waker | Adventure open-sea    | B, Skip EFB ON |
| Mario Kart: Double Dash!! | Racing fun              | A (OpenGL if Vulkan EFB issues) |
| Super Mario Sunshine  | Platformer with water mechanics | B           |
| Animal Crossing       | Life sim relaxing             | A           |
| Tales of Symphonia    | RPG with co-op                | B           |
| Eternal Darkness      | Horror mind-bending           | A           |

**Summary:**
Wii (Dolphin – Mix B/C)

| Game                  | Why Must-Play                  | Tier / Notes |
|-----------------------|--------------------------------|--------------|
| Super Mario Galaxy (1/2) | Platformer masterpiece     | B, Hybrid shaders |
| New Super Mario Bros. Wii | Side-scroller co-op      | A           |
| Mario Kart Wii        | Racing with motion (optional) | B           |
| The Legend of Zelda: Twilight Princess | Epic adventure | B           |
| Punch-Out!!           | Boxing fun                    | A           |
| Harvest Moon: Animal Parade | Farming sim          | A           |

**Summary:**
N64 (Mupen64Plus FZ – Mostly A)

| Game                  | Why Must-Play                  | Tier / Notes |
|-----------------------|--------------------------------|--------------|
| The Legend of Zelda: Ocarina of Time | Timeless adventure   | A, GLideN64 |
| Super Mario 64        | Platforming pioneer            | A           |
| GoldenEye 007         | FPS classic                   | A           |
| Mario Kart 64         | Racing party                  | A           |
| The Legend of Zelda: Majora's Mask | Dark time-loop     | A           |
| Donkey Kong 64        | Collectathon                  | A           |
| Star Fox 64           | Rail shooter                  | A           |
| Kirby 64: The Crystal Shards | Cute platformer     | A           |

**Summary:**
DS/3DS (MelonDS/Azahar – A for DS, B for 3DS)

| Game                  | Why Must-Play                  | Tier / Notes |
|-----------------------|--------------------------------|--------------|
| New Super Mario Bros. (DS) | Side-scroller classic    | A           |
| Mario & Luigi: Bowser's Inside Story (DS) | RPG humor        | A           |
| The Legend of Zelda: A Link Between Worlds (3DS) | Top-down adventure | B, 2x res   |
| Kirby Triple Deluxe (3DS) | Platformer fun          | A           |
| Bravely Default (3DS) | RPG turn-based                | B           |
| Super Street Fighter IV 3D (3DS) | Fighting          | A           |
| Azure Striker Gunvolt (3DS) | Action platformer     | A           |

> [!IMPORTANT]
> **Legal Note:** Only use ROMs from games you own.

## 🤖 About the Replies You'll See Here

Day-to-day upkeep of this guide — replies to issues, clarifications, and
updates — is handled with **Grendizer**, an AI assistant built on this guide,
posting under my account.

- **Grendizer drafts, I decide.** Every reply and guide update is reviewed
  and approved by me before it's posted — typically once a week. If it's
  posted here, my eyes were on it.
- **Every question gets answered — within the week.** Replies no longer
  depend on me having free hours.
- Setups come from my real testing on the Pocket Air Mini. Grendizer works
  from that record and can still miss something: hardware and drivers vary.
  If a fix doesn't work on your unit, say so in an issue — corrections are
  how this guide got good.

Full disclosure pinned on issue #1.

---

## ⚠️ Disclaimer

This guide is for educational purposes only. 
* **Risk:** Modifying system settings, debloating, or using third-party software carries risks. I am not responsible for any damage to your device, software "bricking," or loss of data. Proceed at your own risk.
* **Copyright:** This guide does not provide, host, or link directly to copyrighted ROMs or BIOS files. Emulation is a complex legal area; ensure you own physical copies of the games you emulate and comply with your local laws.
* **Trademarks:** All product names, logos, and brands (Ayaneo, Nintendo, Sony, etc.) are property of their respective owners.

## 🤝 Community Contributions & Credits

This guide has been shaped and improved through valuable community input.

Special thanks to:

- **Nikolai Trukhin (CoolONEOfficial)** — Dolphin configuration insights and optimization contributions.
- **uriuri89** — Community shader recommendations.
- **hardy272** — Additional debloat package suggestions.
- **TheGammaSqueeze** — GammaOS for Pocket Air Mini ([GitHub](https://github.com/TheGammaSqueeze/GammaOSNext)).
- **BruhMeh** — PAM Stock OS Optimization Guide ([GitHub](https://github.com/BruhMeh/PAM-Stock-OS-Optimization-Guide)) and community testing findings.
- **Uri (uriuri89)** — Original author behind the BruhMeh optimization guide; Google Play Services hardening and standby bucket recommendations.

Community feedback continues to help refine performance, stability, and usability across different setups.

### ☕ Final Support
If this "Zero to Hero" guide helped you build the perfect handheld, consider supporting my work!

<a href="https://www.buymeacoffee.com/cyberyellowninja" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

<a href="https://ko-fi.com/cyberyellowninja" target="_blank">
  <img src="https://storage.ko-fi.com/cdn/kofi5.png?v=3"
       alt="Buy Me a Coffee at ko-fi.com"
       style="height: 60px !important; width: 217px !important;"></a>

**Happy Gaming!** 🕹️✨

