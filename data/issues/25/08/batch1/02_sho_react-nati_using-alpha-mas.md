issue title: Using alpha mask over a group of radialgradient shaders leads to some weird compositing
labels: bug
comment count: 0
hyperlink: https://github.com/shopify/react-native-skia/issues/3254
status: open
date opened: 2025-08-02
repo 30d_merge_rate: 22

====

description:
### Description

I have a white to transparent radial gradient in a circle that will act as a mask over three other coloured radial gradients in circles in a group. When it's not a mask everything looks like I expect:

<img width="2272" height="1966" alt="Image" src="https://github.com/user-attachments/assets/ca134892-b580-4cad-97b9-ed02d5dbc477" />
The solid white in the center is the center of the radial gradient - defined colors rgba(255,255,255,1), rgba(255,255,255,0). The three colour circles behind overlap each other and have their own transparency gradients also defined as rgba(r,g,b,1) to rgba(r,g,b,0). 

When the white circle is defined as a Mask the shapes within the group that should be masked seem to get composited as solid objects with the background color appearing where they are transparent (it is not doing this when they are not masked).

<img width="2272" height="1960" alt="Image" src="https://github.com/user-attachments/assets/09e1c96a-0d2c-4eac-975e-11ae555cc9a8" />

I would say it appears as though one solid circle is sitting on top of the other except that you can see the visible edge of both circles under the masked area where if one was on top you'd only see one edge - so I'm struggling to figure out what's going on!

Relevant piece of code is:
```
 <Mask
        mode="alpha"
        mask={
          <Circle key="rs" cx={width / 2} cy={height / 2} r={Math.max(width, height)}>
            <RadialGradient
              c={vec(width / 2, height / 2)}
              r={Math.max(width / 2, height / 2)}
              colors={['rgba(255,255,255,1)', 'rgba(255,255,255,0)']}
            />
          </Circle>
        }
      >
        <Group>
          {colorBlobs.map((blob) => (
            <Circle key={blob.id} cx={blob.cx} cy={blob.cy} r={blob.radius}>
              <RadialGradient
                c={vec(blob.cx, blob.cy)}
                r={blob.radius}
                colors={[
                  `rgba(${blob.color[0]},${blob.color[1]},${blob.color[2]},1)`,
                  `rgba(${blob.color[0]},${blob.color[1]},${blob.color[2]},0)`
                ]}
              />
            </Circle>
          ))}
        </Group>
      </Mask>
```
with the colorBlobs defined thus:
```
const colorBlobs = useMemo(() => {
    const hues = [
      [0, 255, 224],
      [255, 181, 245],
      [59, 255, 251]
    ];

    const positions = [
      [width / 2, height / 2],
      [width / 4, height / 4],
      [(width / 4) * 3, (height / 4) * 3]
    ];

    return Array.from({ length: NUM_COLORS }).map((_, i) => {
      const centerX = positions[i][0];
      const centerY = positions[i][1];
      const radius = width * 0.5;
      return {
        id: `color-${i}`,
        cx: centerX,
        cy: centerY,
        radius,
        color: hues[i % hues.length]
      };
    });
  }, []);
```

I have played around with blendMode both on the Group and in the JSX style `<Blend mode=` wrapped around the RadialGradient - and while some modes would change how they looked none fundamentally fixed it.



### React Native Skia Version

2.0.0-next.4

### React Native Version

0.79.3

### Using New Architecture

- [x] Enabled

### Steps to Reproduce

Create a canvas (web or native but my screenshots are from web using the latest wasm). and render the markup as described above.

Expect the gradient to mask a correctly composited flat group of three coloured blobs. Actual result is that the gradient coloured blobs are getting composited weirdly (technical term).

### Snack, Code Example, Screenshot, or Link to Repository

https://github.com/rsouthgate/skia-bug-repro

Minimal expo-router based repro.

npm start... View on web or through Expo Go - behaviour is the same, toggle mask on or off to see how the two circles blend when not masked vs how they (don't) blend when masked

===
