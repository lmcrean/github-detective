issue title: [Android] gl::Context::makeCurrent Segfault error
labels: bug
comment count: 6
hyperlink: https://github.com/shopify/react-native-skia/issues/3156
status: open
date opened: 2025-05-22
repo 30d_merge_rate: 22

====

description:
### Description

Hello, two of our clients are encountering an issue, sometimes application just crash. This seems to be happening only on low end devices with Android 10 only. In our case:
```
Oppo A15S, Android 10
Blackview BV9900 Pro, Android 10
```

### React Native Skia Version

1.12.4

### React Native Version

0.76.7

### Using New Architecture

- [x] Enabled

### Steps to Reproduce

We're using Skia for many things but most-likely users are having a crash when app renders charts with `victory-native` (version `^41.16.1`) on initial route. I can see by the logs that, most likely app crashes right after opening. Let me know if I can provide somehow more informations that might help resolving this issue.

### Snack, Code Example, Screenshot, or Link to Repository

<img height="500" alt="Image" src="https://github.com/user-attachments/assets/95532d5a-4bd2-4f77-9855-bb5898b034c9" />

<img width="500" alt="Image" src="https://github.com/user-attachments/assets/56efe6e8-0e6e-4620-86eb-6db91d46ee54" />

===

comment #1 by wcandillon, 2025-05-22, 11:39:26
yes please provide me with more information if possible. Is it possible/easy to reproduce? if it always/often happens on these specified devices, I could use [BrowserStack](https://www.browserstack.com/) to debug the issue.

comment #2 by dawidzawada, 2025-05-22, 12:26:30
It is happening only on these 2 devices, by the logs I can see that this occurs on our dashboard tab route, we render there a bar charts with energy usage values, energy prices etc. for each hour at current day. After 2:00 PM we render also values for next day - client says that app crashes only after in the afternoon (and I confirm that by Sentry events too) - so that's probably somehow connected. There's no much difference between chart for only current day and current day & tomorrow, there's only more values to display(48 bars instead or 24).  

Here's the raw stack trace, it is always the same, only differences between each trace are memory addresses.
```
OS Version: Android 10 (CPH2179_11_A.68)
Report Version: 104

Exception Type: Unknown (SIGSEGV)

Application Specific Information:
Segfault

Thread 0 Crashed:
0   split_config.arm64_v8a.apk      0x71885fab98        gl::Context::makeCurrent
1   split_config.arm64_v8a.apk      0x71886c5828        RNSkia::OpenGLWindowContext::getSurface
2   split_config.arm64_v8a.apk      0x71885fd8d4        RNSkia::RNSkOpenGLCanvasProvider::renderToCanvas
3   split_config.arm64_v8a.apk      0x71885f4e68        RNSkia::RNSkPictureRenderer::renderImmediate
4   split_config.arm64_v8a.apk      0x71885f3be0        RNSkia::RNSkAndroidView<T>::surfaceAvailable
5   split_config.arm64_v8a.apk      0x71885f5b28        facebook::jni::detail::MethodWrapper<T>::dispatch
6   split_config.arm64_v8a.apk      0x71885f5a40        facebook::jni::detail::FunctionWrapper<T>::call
7   base.odex                       0x7292be0d30        <unknown> + 492088200496





EOF
```

Also here's how we render our BarChart component:
```typescript
    <>
      <YAxis
        chartHeight={
          chartRef.current?.chartHeight ?? chartHeight + TOP_PADDING_DOMAIN
        }
        gridlinesData={gridlinesData}
        unit={unit}
        font={font}
      />

      <ScrollView
        ref={scrollViewRef}
        horizontal
        style={{ width: Dimensions.get('window').width }}
        contentContainerStyle={{
          height: chartHeight,
          width: newChartWidth,
        }}
        showsHorizontalScrollIndicator={false}
        onLayout={() => handleScroll(tooltipIndex ?? highlightIndex)}
        bounces={false}
        scrollEventThrottle={16}
      >
        <Pressable onPress={handleTouchStart} style={styles.pressContainer}>
          <BarToolTip
            sharedX={tooltipConfig.sharedX}
            sharedY={tooltipConfig.sharedY}
            tooltipText={tooltipConfig.description}
            activeItem={tooltipConfig.activeItem}
            negative={
              tooltipConfig.indexValue <= 0 ? chartRef.current?.yScale(0) : null
            }
            defaultTooltip={defaultTooltip}
            offset={labelOffset}
          />

          <CartesianChart
            data={data}
            xKey='time'
            yKeys={['value', 'xPos', 'referenceValue']}
            padding={5}
            domainPadding={{
              left: CHART_PADDING_HORIZONTAL * (renderYAxis ? 2 : 4),
              right: labelWidth,
              bottom: 0,
              top: renderYAxis ? 0 : TOP_PADDING_DOMAIN,
            }}
            domain={{
              y: [
                gridlines[0],
                gridlines[gridlines.length - 1] * Y_SCALE_FACTOR,
              ],
            }}
            xAxis={{
              font,
              tickCount: data.length - 1,
              lineWidth: 0,
              labelPosition: 'outset',
              labelColor: chartXAxisColor,
              labelOffset: 6,
              formatXLabel: (label) => (label ? label : ''),
            }}
            yAxis={[
              {
                yKeys: ['value', 'referenceValue', 'xPos'],
                font,
                tickValues: gridlines,
                tickCount: gridlines.length,
                axisSide: 'right',
                labelPosition: 'outset',
                labelColor: chartYAxisColor,
              },
            ]}
            chartPressState={state}
            onChartBoundsChange={chartPropsHandle}
            actionsRef={chartActionsRef}
            customGestures={composed}
            chartPressConfig={{
              pan: { activateAfterLongPress: ACTIVATE_AFTER_LONG_PRESS },
            }}
          >
            {({ points, chartBounds, yScale, xScale }) => {
              chartRef.current = {
                chartHeight: chartBounds.bottom - chartBounds.top,
                yScale,
                xScale,
              }

              return points.value.map((point, index) => {
                const referenceValue = roundToDecimalPlaces(
                  points.referenceValue[index]?.yValue ?? 0,
                  2
                )
                const value = roundToDecimalPlaces(
                  points.value[index]?.yValue ?? 0,
                  2
                )

                const showDottedBar =
                  isBalance && referenceValue !== 0 && referenceValue !== value

                return (
                  <React.Fragment key={index}>
                    {((activeItemTooltip?.index !== null &&
                      activeItemTooltip?.index === index) ||
                      index === highlightIndex) && (
                      <>
                        {/* highlight bar */}
                        {showHighlight && index === highlightIndex && (
                          <>
                            <Rect
                              x={point.x - getPxSize(17)}
                              y={yScale(gridlines[gridlines.length - 1])}
                              height={chartBounds.bottom - chartBounds.top}
                              width={getPxSize(34)}
                              key={'h' + index.toString()}
                              color={
                                isHighlightGreen ? barCheapHighlight : barColor
                              }
                            />
                          </>
                        )}
                      </>
                    )}
                    {showDottedBar && (
                      <DottedBar
                        barWidth={17}
                        barHeight={
                          yScale(0) - Number(points.referenceValue[index].y)
                        }
                        xPoint={point.x - 8.5}
                        yPoint={Number(points.referenceValue[index].y)}
                        color={dottedBarColor}
                      />
                    )}

                    {/* default bar */}
                    <Bar
                      chartBounds={chartBounds} // 👈 chartBounds is needed to know how to draw the bars
                      points={[point]} // 👈 points is an object with a property for each yKey
                      roundedCorners={{
                        topLeft: cornerRadius,
                        topRight: cornerRadius,
                      }}
                      barWidth={16}
                      color={getBarColor(index)}
                    />
                  </React.Fragment>
                )
              })
            }}
          </CartesianChart>
        </Pressable>
      </ScrollView>
    </>
```

comment #3 by wcandillon, 2025-06-17, 08:51:17
Can you send me a standalone example? I would be curious to try it on browserstack

comment #4 by dawidzawada, 2025-06-18, 17:20:32
I'll try to provide it as soon as possible, it's on our backlog. I was able to reproduce this on BrowserStack only on Oppo Reno 3 Pro that has Android 10. Here's a logcat, it is happening when app is trying to render a BarChart:
```
Device Selected: Oppo Reno 3 Pro v10.0
Connecting to real device cloud
Starting device Oppo Reno 3 Pro v10.0
Downloading app on Oppo Reno 3 Pro v10.0
Installing app on Oppo Reno 3 Pro v10.0
Starting app on Oppo Reno 3 Pro v10.0
06-18 16:58:53.169 W/ColorExSystemServiceHelper(11688): checkColorExSystemService intent getComponent is null
06-18 16:58:53.706 W/BridgelessReactContext(11688): [WARNING] Bridgeless doesn't support CatalystInstance. Accessing an API that's not part of the new architecture is not encouraged usage.
06-18 16:58:53.768 W/pool-23-thread-(11688): type=1400 audit(0.0:5970): avc: denied { read } for name="version" dev="proc" ino=4026532137 scontext=u:r:untrusted_app:s0:c251,c290,c512,c768 tcontext=u:object_r:proc_version:s0 tclass=file permissive=0
06-18 16:58:54.205 W/[RNScreens](11688): backTitleVisible prop is not available on Android
06-18 16:58:54.206 W/[RNScreens](11688): backTitleFontFamily prop is not available on Android
06-18 16:58:54.206 W/[RNScreens](11688): disableBackButtonMenu prop is not available on Android
06-18 16:58:54.206 W/[RNScreens](11688): largeTitleFontFamily prop is not available on Android
06-18 16:58:54.206 W/[RNScreens](11688): largeTitleFontWeight prop is not available on Android
06-18 16:58:54.206 W/[RNScreens](11688): largeTitleHideShadow prop is not available on Android
06-18 16:58:54.563 W/unknown:ViewManagerPropertyUpdater(11688): Could not find generated setter for class com.facebook.react.uimanager.RootViewManager
06-18 16:58:54.577 W/[RNScreens](11688): backTitleVisible prop is not available on Android
06-18 16:58:54.577 W/[RNScreens](11688): backTitleFontFamily prop is not available on Android
06-18 16:58:54.578 W/[RNScreens](11688): disableBackButtonMenu prop is not available on Android
06-18 16:58:54.578 W/[RNScreens](11688): largeTitleFontFamily prop is not available on Android
06-18 16:58:54.578 W/[RNScreens](11688): largeTitleFontWeight prop is not available on Android
06-18 16:58:54.578 W/[RNScreens](11688): largeTitleHideShadow prop is not available on Android
06-18 16:58:54.581 W/View    (11688): requestLayout() improperly called by com.swmansion.rnscreens.Screen{7d98757 V.E...... ......ID 0,0-1080,2268 #12} during layout: running second layout pass
06-18 16:58:54.592 W/.bankilo.pstryk(11688): type=1400 audit(0.0:5971): avc: denied { read } for name="u:object_r:debug_bq_dump_prop:s0" dev="tmpfs" ino=17440 scontext=u:r:untrusted_app:s0:c251,c290,c512,c768 tcontext=u:object_r:debug_bq_dump_prop:s0 tclass=file permissive=0
06-18 16:58:54.596 E/libc    (11688): Access denied finding property "vendor.debug.bq.dump"
06-18 16:58:54.597 E/libc    (11688): Access denied finding property "vendor.debug.bq.dump"
06-18 16:58:54.597 E/libc    (11688): Access denied finding property "vendor.debug.bq.dump"
06-18 16:58:54.592 W/.bankilo.pstryk(11688): type=1400 audit(0.0:5973): avc: denied { read } for name="u:object_r:debug_bq_dump_prop:s0" dev="tmpfs" ino=17440 scontext=u:r:untrusted_app:s0:c251,c290,c512,c768 tcontext=u:object_r:debug_bq_dump_prop:s0 tclass=file permissive=0
06-18 16:58:54.610 W/Gralloc3(11688): mapper 3.x is not supported
06-18 16:58:54.613 W/Gralloc3(11688): allocator 3.x is not supported

```

comment #5 by wcandillon, 2025-06-21, 11:15:43
this looks interesting, can you send me the example above as a standalone example that I can run/test directly? 

comment #6 by JennieCrowel, 2025-07-15, 13:46:22
Hi, did you have any progress on this?
I experienced the same issue and app crash on Android 9. 

` #00  pc 0x000000000019f46c  /data/app/blabla-kTjdFpQdtYdGtbp0skN5XQ==/split_config.armeabi_v7a.apk (gl::Context::makeCurrent(gl::Surface const*)+12)`

In my opinion, the application attempted to begin drawing with OpenGL on a surface that wasn’t yet ready or compatible for rendering, which caused the crash.
