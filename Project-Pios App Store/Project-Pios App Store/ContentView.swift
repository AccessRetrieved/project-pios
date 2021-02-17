//
//  ContentView.swift
//  Project-Pios App Store
//
//  Created by Jerry Hu on 2021/2/17.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationView {
            List {
                NavigationLink(destination: HomeView()) {
                    HStack {
                        Text("Home").font(.headline)
                    }
                }
                
                NavigationLink(destination: Store()) {
                    HStack {
                        Text("Store")
                    }
                }
            }.environment(\.defaultMinListRowHeight, 25)
            
            // Adds a copy of HomeView so that the homescreen can be displayed on launch
            Text("App store for project-pios. Click store to get started").font(.title3)
            
        }.frame(width: 700, height: 500)
    }
}

struct HomeView: View {
    var body: some View {
        Text("Home").font(.title).offset(x: -230, y: -210)
        Text("App store for project-pios. Click store to get started").font(.title3)
        
        Image(systemName: "arrow.left.circle").offset(x: -250, y: -220).font(.headline)
    }
}

struct Store: View {
    var body: some View {
        NavigationView {
            List {
                NavigationLink(destination: installOCR()) {
                    HStack {
                        Text("Optical Characters Recognition").multilineTextAlignment(.center)
                    }
                }
                
                NavigationLink(destination: installQR()) {
                    HStack {
                        Text("Qr Code Scanner").multilineTextAlignment(.center)
                    }
                }
            }.environment(\.defaultMinListRowHeight, 30)
        }
    }
}

struct installOCR: View {
    var body: some View {
        Text("Optical Characters Recognition").font(.title).offset(x: 0, y: -200)
        Text("OCR is an ability to recognize text on screen(with screenshot function). Built with Python3.9")
    }
}

struct installQR: View {
    var body: some View {
        Text("Qr Code Scanner").font(.title).offset(x: 0, y: -200)
        VStack {
            ZStack {
                Text("Qr Code Scanner passes an image with extension jpg or png, and scans qr code in image. If none, returns nil(swift) or None(python).")
            }
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
