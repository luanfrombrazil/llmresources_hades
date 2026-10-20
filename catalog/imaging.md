# Catálogo HADES — pacote `hades.models.imaging`

Gerado automaticamente a partir do `hades.jar` (parâmetros PADRÃO). Componentes marcados com ✅ têm documentação detalhada em `components/`.
Para os demais: portas, posições e bbox valem para os parâmetros padrão; componentes de largura variável mudam com `n_bits`. Antes de usar um deles pela primeira vez, documente-o (veja `ADICIONANDO_COMPONENTES.md`).

## ANDFilter

`hades.models.imaging.ANDFilter` — per-pixel per-color logical AND of the two input images.

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1800), `Y` out 1b @(1800,1200)

## AbsSubFilter

`hades.models.imaging.AbsSubFilter` — per-pixel per-component absolute difference.

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1800), `Y` out 1b @(1800,1200)

## AddFilter

`hades.models.imaging.AddFilter` — per-pixel per-component addition of two input images:

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1800), `Y` out 1b @(1800,1200)

## AffineTransformationFilter

`hades.models.imaging.AffineTransformationFilter` — general affine transformation (scaling, rotation, shearing).

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  1.0 0.0 0.0 1.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## BlueFilter

`hades.models.imaging.BlueFilter` — color image filter for the blue channel, (r,g,b -> 0,0,b)

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## CatHFilter

`hades.models.imaging.CatHFilter` — horizontal concatenation of two input images.

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1800), `Y` out 1b @(1800,1200)

## CatVFilter

`hades.models.imaging.CatVFilter` — vertical concatentation.

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1800), `Y` out 1b @(1800,1200)

## ConstantColorFilter

`hades.models.imaging.ConstantColorFilter` — generate the user-selected constant color. 

- Parâmetros padrão: `1001 200 200 200 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## ConvolutionFilter

`hades.models.imaging.ConvolutionFilter` — Base class for all convolution image filters. Kernel:

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## CropFilter

`hades.models.imaging.CropFilter` — Image filter to crop a subimage from a larger image;

- Parâmetros padrão: `1001 0 0 100 100 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## DifferenceFilter

`hades.models.imaging.DifferenceFilter` — An image filter to calculate the (absolute) difference

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1800), `Y` out 1b @(1800,1200)

## EdgeNEFilter

`hades.models.imaging.EdgeNEFilter` — Edge-detection 3x3 convolution filter (north-east direction):

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## EdgeNWFilter

`hades.models.imaging.EdgeNWFilter` — Edge-detection 3x3 convolution filter (north-west direction):

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## EdgeXFilter

`hades.models.imaging.EdgeXFilter` — Edge-detection 3x3 convolution filter (x direction):

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## EdgeYFilter

`hades.models.imaging.EdgeYFilter` — Edge-detection 3x3 convolution filter (y direction):

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## EqualsFilter

`hades.models.imaging.EqualsFilter` — Per-pixel equality test and mask generator. The output image

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1800), `Y` out 1b @(1800,1200)

## EqualsWithinFilter

`hades.models.imaging.EqualsWithinFilter` — Per-pixel per-component 'fuzzy' equality test with user-settable

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1800), `Y` out 1b @(1800,1200)

## GammaFilter

`hades.models.imaging.GammaFilter` — Per-pixel gamma correction (gamma, brightness, offset).

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  2.5 10.0 0.9 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## Gauss3Filter

`hades.models.imaging.Gauss3Filter` — Gauss-convolution image filter. Kernel:

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## Gauss5Filter

`hades.models.imaging.Gauss5Filter` — Gauss-convolution image filter. Kernel:

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## GaussFilter

`hades.models.imaging.GaussFilter` — Gauss convolution image filter. 

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## GradientColorFilter

`hades.models.imaging.GradientColorFilter` — generates a 2D color-gradient output image which interpolates

- Parâmetros padrão: `1001 200 200 255 255 255 0 0 0  255.0 0.0 0.0 0.0 255.0 0.0 0.0 0.0 255.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## GrayFilter

`hades.models.imaging.GrayFilter` — Color image filter, (r,g,b) -> (gray,gray,gray)

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## GreenFilter

`hades.models.imaging.GreenFilter` — Green-channel extraction filter, (r,g,b) -> (0,g,0)

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## GridFilter

`hades.models.imaging.GridFilter` — Overlay a parametrized grid on the input image.

- Parâmetros padrão: `1001 50 255 255 255 170 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## ImageMux21

`hades.models.imaging.ImageMux21` — A 2:1 multiplexer for images.

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(2400, 2400)
- Portas: `Y` out 1b @(2400,1200), `A0` in 1b @(0,1800), `A1` in 1b @(0,600), `S` in 1b @(1200,2400)

## ImageSource

`hades.models.imaging.ImageSource` — load images from files or URLs.

- Parâmetros padrão: `1001 null`
- bbox: (-2400, -600)..(0, 600)
- Portas: `Y` out 1b @(0,0)

## ImageViewer

`hades.models.imaging.ImageViewer` — simple Swing-based image viewer with zoom

- Parâmetros padrão: `1001`
- bbox: (0, -600)..(2400, 600)
- Portas: `A` in 1b @(0,0)

## ImageWriter

`hades.models.imaging.ImageWriter` — write image data in PPM format to an output file.

- Parâmetros padrão: `1001 null`
- bbox: (0, -600)..(2400, 600)
- Portas: `A` in 1b @(0,0)

## InsideRangeFilter

`hades.models.imaging.InsideRangeFilter` — Per-pixel per-component range comparison; the filter

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## InvertFilter

`hades.models.imaging.InvertFilter` — Color inversion filter, (r,g,b) -> (255-r,255-g,255-b)

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## InvertLookupFilter

`hades.models.imaging.InvertLookupFilter` — Color inversion filter based on LookupTable,

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## Laplace3Filter

`hades.models.imaging.Laplace3Filter` — Laplace convolution image filter. Kernel:

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## LookupFilter

`hades.models.imaging.LookupFilter` — Base class for lookup-table based image filters.

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## MaxFilter

`hades.models.imaging.MaxFilter` — Per-pixel per-component max operation:

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1800), `Y` out 1b @(1800,1200)

## MinFilter

`hades.models.imaging.MinFilter` — Per-pixel per-component minimum operation:

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1800), `Y` out 1b @(1800,1200)

## MirrorXFilter

`hades.models.imaging.MirrorXFilter` — mirrors the input image left-right.

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## MirrorYFilter

`hades.models.imaging.MirrorYFilter` — mirrors the input image top-down.

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## MultFilter

`hades.models.imaging.MultFilter` — Per-pixel per-component multiplication.

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1800), `Y` out 1b @(1800,1200)

## ORFilter

`hades.models.imaging.ORFilter` — Per-pixel per-component logical OR of two input images.

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1800), `Y` out 1b @(1800,1200)

## OffsetFilter

`hades.models.imaging.OffsetFilter` — Offset image filter based on lookup-tables.

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## ParametrizedFilter

`hades.models.imaging.ParametrizedFilter` — Base class for simple per-pixel image filters.

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- Portas: `A` in 1b (sem posição), `Y` out 1b (sem posição)

## PerspectiveTransformationFilter

`hades.models.imaging.PerspectiveTransformationFilter` — A perspective transformation (nearest-neighbor sampling).

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  1.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## PurpleDetectionFilter

`hades.models.imaging.PurpleDetectionFilter` — A filter to detect 'purple' colors in input images; 

- Parâmetros padrão: `1001 50 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## RandomFilter

`hades.models.imaging.RandomFilter` — Generate an output image with random pixel values.

- Parâmetros padrão: `1001 0 255 0 255 0 255 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## RedFilter

`hades.models.imaging.RedFilter` — Red-channel color extraction filter, (r,g,b) -> (r,0,0)

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## ResizeFilter

`hades.models.imaging.ResizeFilter` — Image filter to change image size to the specified dimensions,

- Parâmetros padrão: `1001 100 100 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## RotationFilter

`hades.models.imaging.RotationFilter` — Image filter to rotate the input image via AffineTransformation.

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  45.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## SaturationFilter

`hades.models.imaging.SaturationFilter` — A per-pixel color saturation filter.

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  1.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## SelectRegionFilter

`hades.models.imaging.SelectRegionFilter` — Create a black and white mask from the selected region

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## ShearFilter

`hades.models.imaging.ShearFilter` — ShearFilter - apply an affine transformation to the image.

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.1 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## SimpleFilter

`hades.models.imaging.SimpleFilter` — Base class of per-pixel based image filters.

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## Smooth20Filter

`hades.models.imaging.Smooth20Filter` — Smoothing via 20x20 [1,1,...1] matrix convolution

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## Smooth50Filter

`hades.models.imaging.Smooth50Filter` — Smoothing via 50x50 [1,1,...1] matrix convolution

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## Smooth5Filter

`hades.models.imaging.Smooth5Filter` — Smoothing via 5x5 convolution:

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## SobelXFilter

`hades.models.imaging.SobelXFilter` — Sobel 3x3 convolution image filter (x direction). Kernel:

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## SobelYFilter

`hades.models.imaging.SobelYFilter` — Sobel 3x3 convolution image filter (y direction). Kernel:

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## SubFilter

`hades.models.imaging.SubFilter` — Per-pixel per-component subtraction:

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 2400)
- Portas: `A` in 1b @(0,600), `B` in 1b @(0,1800), `Y` out 1b @(1800,1200)

## ThresholdFilter

`hades.models.imaging.ThresholdFilter` — Per-pixel per-component comparison with user-settable thresholds:

- Parâmetros padrão: `1001 0 0 0 0 0 0 0 0  0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0`
- bbox: (0, 0)..(1800, 1200)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600)

## TriggeredFilter

`hades.models.imaging.TriggeredFilter` — A filter that passes its input image on the rising-edge

- Parâmetros padrão: `1001`
- bbox: (0, 0)..(1800, 1800)
- Portas: `A` in 1b @(0,600), `Y` out 1b @(1800,600), `CLK` in 1b @(0,1200)
