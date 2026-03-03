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

## 🛠️ Phase 1: Preparation & Materials

Before we begin, ensure you have the following ready:
* **The Device:** Ayaneo Pocket Air Mini (charged to at least 60%).
* **Storage:** A high-quality MicroSD card (128GB to 512GB+ recommended).
* **Software:** Download these apps from the Play Store or their official sites:
  * **Frontend:** ES-DE (EmulationStation Desktop Edition)
  * **File Managers:** MiXplorer or ZArchiver
  * **Torrent Manager:** Flud
  * **Editors:** QuickEdit
  * **System Tools:** AccuBattery, Shizuku, Termux
  * **Emulators:** RetroArch, Dolphin, NetherSX2, PPSSPP, Duckstation, Azahar, MelonDS, Mupen64Plus FZ.

---

## 🍳 Phase 2: Mixing the Ingredients (The Recipe for Success)

### **1. System & Firmware Updates**
Ensure the "brain" of your device is up to date.
1. Open the **System Update** app. Install all updates and **Restart**.
2. Open the **Ayasettings** app. Perform the internal update and **Restart** again.

### **2. Virtual Memory Booster**
Crucial for heavy systems like PS2 or Switch:
1. Open **Ayasettings**.
2. Go to **Device -> Virtual Memory Management**.
3. Set the value to **3GB** and enable the **Swap** switch below it.

### **3. Setting up Flud (The Download Manager)**
1. Open **Flud** and grant permissions.
2. Tap the Menu (top left) -> Select **SD Card**.
3. Navigate to the `Downloads` folder.
4. Tap the **"+" folder icon** (top right), name it `Flud`, and select **"Use this folder"**.

---

## 📂 Phase 3: Finding Your Library (The Directions)

I cannot provide direct links, but I can show you the way.

* **The Starter Pack:** Search Google for **"tiny best set: go! archive"**.
  * Look for the **94 GB** version.
  * Download the **Torrent file** from the bottom of the page and open it with Flud.
* **The Holy Grail:** Remember the keyword **"Megathread"**. It is the paradise for retro gamers looking for specific console ROMs and BIOS files.

---

## 🎨 Phase 4: ES-DE Initial Setup & Folders

1. Open **ES-DE**.
2. **Data Directory:** Select your **SD Card** -> Create folder `ES-DE` -> Select **"Use this folder"**.
3. **ROMs Directory:** Select your **SD Card** -> Create folder `ROMS` -> Select **"Use this folder"**.
4. Tap **"Create them"**, then **"I understand"**. Once finished, **fully close** the app.

### **Organizing BIOS & ROMs**
Using **ZArchiver**, navigate to your downloaded `tiny set best go-games`:
1. **BIOS:** Copy everything from the `bios` folder and the `expansion-64` folder inside the zip to the `BIOS` folder on your **SD Card**.
2. **ROMs:** Move game files into their corresponding folders inside the `ROMS` directory on your SD card. 
3. **Pro Tip:** Delete the zip files after extraction to save space!
## ⚙️ Phase 5: Emulator Configuration (The Pro Setup)

### **1. RetroArch (Multi-System Hub)**
Open RetroArch and grant permissions.
* **Visuals:** Settings > User Interface > On-Screen Notifications > Scale Graphics Widgets Automatically: **OFF** | Graphics Widgets Scale Override: **0.75x**.
* **Controls:** Settings > Input > Retropad Binds > Port 1 > Analog to Digital Type: **Left Analog**.
* **Hotkeys (L3 as Enable Button):**
    * Menu Toggle: **L3 + R3** | Quit: **Start + L1** | Fast Forward: **R2** | Slow Motion: **L2**.
    * **Save State: R1** | **Load State: L1** | Screenshots: **Y**.
* **Directories:** Settings > Directory. Point **System/BIOS**, **Saves**, and **Save States** to their respective folders on your **SD Card**.
* **Speed Hack:** Open `Android/data/com.retroarch.aarch64/files/retroarch.cfg` with **QuickEdit**. Add `input_threaded = "false"` at the bottom.
* **Shaders:** Use `LCD-Grid-V2` for Handhelds and `CRT-Lottes` for TV consoles. Avoid "Mega Bezel".

> [!TIP]
> CRT-Lottes is visually accurate but heavier.
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
> **Mario Kart Double Dash Fix:** If you experience a blue overlay during gameplay, it is a Vulkan EFB quirk. To fix it, go to **Dolphin Hacks** and disable (**OFF**) the setting **"Store EFB Copies to Texture Only"**.

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

### **1. Developer Performance Tweaks**
Go to **Settings > System > Developer Options**:
* **Window/Transition/Animator Scale:** Set all to **0x (Off)**.
* **Background Process Limit:** Set to **2**.
* **Disable HW Overlays:** **ON**.

   > [!NOTE]
> On Android 11, Background Process Limit resets after a full shutdown (cold boot).  
> Sleep mode does not reset it.  
> If you power the device off completely, you will need to set it again.

### **2. Battery Health (AccuBattery)**
1. Open **AccuBattery**.
2. Set the **Charge Alarm to 80%**.
3. Always unplug at 80% to maximize the lifespan of your PAM's internal battery.

---

---

## 🚀 Phase 7.5: Performance & Audio Optimization Profiles

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

## 📱 Phase 9: Removing Touch Overlays

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

Community feedback continues to help refine performance, stability, and usability across different setups.

### ☕ Final Support
If this "Zero to Hero" guide helped you build the perfect handheld, consider supporting my work!

<a href="https://www.buymeacoffee.com/cyberyellowninja" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

<a href="https://ko-fi.com/cyberyellowninja" target="_blank">
  <img src="https://storage.ko-fi.com/cdn/kofi5.png?v=3"
       alt="Buy Me a Coffee at ko-fi.com"
       style="height: 60px !important; width: 217px !important;"></a>

**Happy Gaming!** 🕹️✨
